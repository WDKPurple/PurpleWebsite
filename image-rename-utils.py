#!/usr/bin/env python

import re
import sys
import os.path
import os
import io
import shutil
import hashlib

#  rename-images <src_pattern> <dest_pattern>
#                                       rename images

def usage():
	print("""Usage: %s <options>... <command>

Available commands:
  search-image [<pattern>]             search images in all posts
  list-image <file>                    list unique images in a post file
  rename-image <old> <new>             rename an images
  batch-rename <file> [<dest_pattern>] batch rename images in a post file
                                       NOTE: dest_pattern is without extension
  batch-rename-mult <post_pattern> [<dest_pattern>]
                                       batch rename images in post files
  list-unused-images                   list unused images
  list-duplicated-images               list duplicated images

Example of dest_pattern: default is {date}/{date2}_%%03d
  {date}                               the first 10 character of the file name
  {date2}                              {date} with "-" removed
  {name}                               the file name without extension

Available options:
  --select-image <pattern>             select image by pattern
  --exclude-image <pattern>            exclude image by pattern
  --select-index <pattern>             select image in a post file by index
  --exclude-index <pattern>            exclude image in a post file by index
  --select-post <pattern>              select post by pattern
  --exclude-post <pattern>             exclude post by pattern
  --dry-run                            do not perform actual operations
  --post-path <path>                   set the path to posts, default is
                                       ./content/post/
  --image-path <path>                  set the path to images, default is
                                       ../StaticResources/images/""" % sys.argv[0])
	sys.exit(1)


def parse_index(s):
	ret = []
	for ss in s.split(","):
		i = ss.find("-")
		if i >= 0:
			ss1 = ss[:i]
			ss2 = ss[i+1:]
			ret.append([int(ss1) if len(ss1) > 0 else 1, int(ss2) if len(ss2) > 0 else 2147483647])
		else:
			i = int(ss)
			ret.append([i, i])
	return ret


def search_image_in_one_file(select_image, exclude_image, select_index, exclude_index, file, callback, userdata, deduplicate):
	line_number = 0
	index = 0
	known_images = set()

	for line in file:
		line_number += 1
		images = re.findall(r'images/(.+?\.(?:png|jpg|gif|webp))', line)

		for image in images:
			if deduplicate:
				if image in known_images:
					continue
				known_images.add(image)

			index += 1
			match = True

			# check select_image
			if len(select_image) > 0:
				match = False
				for patt in select_image:
					if re.search(patt, image):
						match = True
						break
				if not match:
					continue

			# check exclude_image
			for patt in exclude_image:
				if re.search(patt, image):
					match = False
					break
			if not match:
				continue

			# check select_index
			if len(select_index) > 0:
				match = False
				for idx in select_index:
					if index >= idx[0] and index <= idx[1]:
						match = True
						break
				if not match:
					continue

			# check exclude_index
			for idx in exclude_index:
				if index >= idx[0] and index <= idx[1]:
					match = False
					break
			if not match:
				continue

			callback(userdata, line_number, index, image)


def search_image_in_posts_0(select_image, exclude_image, select_post, exclude_post, post_path, callback):
	for dirpath, dirnames, filenames in os.walk(post_path):
		for name in filenames:
			match = True

			# check select_post
			if len(select_post) > 0:
				match = False
				for patt in select_post:
					if re.search(patt, name):
						match = True
						break
				if not match:
					continue

			# check exclude_post
			for patt in exclude_post:
				if re.search(patt, name):
					match = False
					break
			if not match:
				continue

			try:
				with open(os.path.join(dirpath, name), "rU") as file:
					search_image_in_one_file(select_image, exclude_image, [], [], file, callback, name, False)
			except Exception as e:
				print "ERROR: Failed to open file '%s':" % name
				print repr(e)


def search_image_in_posts(select_image, exclude_image, select_post, exclude_post, post_path):
	def callback(userdata, line_number, index, image):
		print "%s:%d:%s" % (userdata, line_number, image)
	search_image_in_posts_0(select_image, exclude_image, select_post, exclude_post, post_path, callback)


def list_image_in_one_post(select_image, exclude_image, select_index, exclude_index, filename):
	def callback(userdata, line_number, index, image):
		print "%d L%d:%s" % (index, line_number, image)
	try:
		with open(filename, "rU") as file:
			search_image_in_one_file(select_image, exclude_image, select_index, exclude_index, file, callback, None, True)
	except Exception as e:
		print "ERROR: Failed to open file '%s':" % filename
		print repr(e)


def rename_images(post_path, image_path, images, dry_run):
	count = 0
	for image in images:
		if image[0] == image[1]:
			continue
		count += 1
		print "'%s' ==> '%s'" % (image[0], image[1])
		src = os.path.join(image_path, image[0])
		if not os.path.isfile(src):
			print "WARNING: source file does not exist"
		if not dry_run:
			dest = os.path.join(image_path, image[1])
			dest_dir = dest.replace("\\", "/")
			idx = dest_dir.rfind("/")
			if idx > 0:
				try:
					os.makedirs(dest_dir[:idx])
				except:
					pass
			try:
				shutil.move(src, dest)
			except Exception as e:
				print "ERROR: Failed to move file:"
				print repr(e)

	if count == 0:
		return

	for dirpath, dirnames, filenames in os.walk(post_path):
		for name in filenames:
			s = ""
			try:
				with open(os.path.join(dirpath, name), "rb") as file:
					s = file.read()
			except Exception as e:
				print "ERROR: Failed to open file '%s':" % filename
				print repr(e)
			if len(s) == 0:
				continue
			s_new = s
			for image in images:
				if image[0] == image[1]:
					continue
				s_new = s_new.replace(
					("images/" + image[0]).replace('\\', '/').replace('//', '/'),
					("images/" + image[1]).replace('\\', '/').replace('//', '/'))
			if s_new != s:
				print "File '%s' changed" % name
				if not dry_run:
					try:
						with open(os.path.join(dirpath, name), "wb") as file:
							file.write(s_new)
					except Exception as e:
						print "ERROR: Failed to save file '%s':" % filename
						print repr(e)


def get_rename_image_list_by_pattern(src_images, pattern, filename):
	name_str = filename.replace("\\", "/")
	idx = name_str.rfind("/")
	name_str = name_str[idx+1:] if idx >= 0 else name_str
	idx = name_str.rfind(".")
	name_str = name_str[:idx] if idx >= 0 else name_str
	date_str = name_str[:10]
	date_str2 = date_str.replace("-", "")

	images = []
	index = 0
	for image in src_images:
		index += 1
		idx = image.rfind(".")
		ext = image[idx:] if idx >= 0 else ""
		dest = (pattern % index) + ext
		dest = dest.replace("{date}", date_str).replace("{date2}", date_str2).replace("{name}", name_str)
		images.append([image, dest])
	return images


def get_rename_image_list_in_one_post(pattern, select_image, exclude_image, select_index, exclude_index, filename):
	src_images = []
	def callback(userdata, line_number, index, image):
		src_images.append(image)
	try:
		with open(filename, "rU") as file:
			search_image_in_one_file(select_image, exclude_image, select_index, exclude_index, file, callback, None, True)
	except Exception as e:
		print "ERROR: Failed to open file '%s':" % filename
		print repr(e)
	return get_rename_image_list_by_pattern(src_images, pattern, filename)


def get_rename_image_list_in_posts(pattern, select_image, exclude_image, select_post, exclude_post, post_path):
	images = []
	for dirpath, dirnames, filenames in os.walk(post_path):
		for name in filenames:
			match = True

			# check select_post
			if len(select_post) > 0:
				match = False
				for patt in select_post:
					if re.search(patt, name):
						match = True
						break
				if not match:
					continue

			# check exclude_post
			for patt in exclude_post:
				if re.search(patt, name):
					match = False
					break
			if not match:
				continue

			images += get_rename_image_list_in_one_post(pattern, select_image, exclude_image, [], [], os.path.join(dirpath, name))

	return images


def list_unused_images(select_image, exclude_image, select_post, exclude_post, post_path, image_path):
	known_images = set()

	def callback(userdata, line_number, index, image):
		if not image in known_images:
			known_images.add(image)
	search_image_in_posts_0(select_image, exclude_image, select_post, exclude_post, post_path, callback)

	for dirpath, dirnames, filenames in os.walk(image_path):
		for name in filenames:
			match = True

			# check select_image
			if len(select_image) > 0:
				match = False
				for patt in select_image:
					if re.search(patt, image):
						match = True
						break
				if not match:
					continue

			# check exclude_image
			for patt in exclude_image:
				if re.search(patt, image):
					match = False
					break
			if not match:
				continue

			relname = os.path.relpath(os.path.join(dirpath, name), image_path).replace("\\", "/")
			if not relname in known_images:
				print relname


def list_duplicated_images(select_image, exclude_image, select_post, exclude_post, post_path, image_path):
	known_images = {}

	def callback(userdata, line_number, index, image):
		s = "    %s:%d" % (userdata, line_number)
		if image in known_images:
			known_images[image].append(s)
		else:
			known_images[image] = [s]
	search_image_in_posts_0(select_image, exclude_image, select_post, exclude_post, post_path, callback)

	known_hashes = {}

	for dirpath, dirnames, filenames in os.walk(image_path):
		for name in filenames:
			match = True

			# check select_image
			if len(select_image) > 0:
				match = False
				for patt in select_image:
					if re.search(patt, image):
						match = True
						break
				if not match:
					continue

			# check exclude_image
			for patt in exclude_image:
				if re.search(patt, image):
					match = False
					break
			if not match:
				continue

			absname = os.path.join(dirpath, name)
			relname = os.path.relpath(absname, image_path).replace("\\", "/")
			hash = hashlib.sha1()
			try:
				with open(absname, "rb") as file:
					data = file.read()
					hash.update(data)
				hash = "size:%d sha1:%s" % (len(data), hash.hexdigest())
				if hash in known_hashes:
					known_hashes[hash].append(relname)
				else:
					known_hashes[hash] = [relname]
			except Exception as e:
				print "ERROR: Failed to open file '%s':" % absname
				print repr(e)

	for hash in known_hashes:
		image_list = known_hashes[hash]
		if len(image_list) > 1:
			print "%s(%d):" % (hash, len(image_list))
			for image in image_list:
				if image in known_images:
					lst = known_images[image]
					print "  %s(%d):" % (image, len(lst))
					for s in lst:
						print s
				else:
					print "  %s(0):" % image

def main():
	select_image = []
	exclude_image = []
	select_index = []
	exclude_index = []
	select_post = []
	exclude_post = []
	dry_run = False
	post_path = "./content/post/"
	image_path = "../StaticResources/images/"

	# parse options
	i = 1
	m = len(sys.argv)
	while i < m:
		if not sys.argv[i].startswith("-"):
			break
		elif sys.argv[i] == "--select-image":
			i += 1
			if i >= m:
				usage()
			select_image.append(sys.argv[i])
		elif sys.argv[i] == "--exclude-image":
			i += 1
			if i >= m:
				usage()
			exclude_image.append(sys.argv[i])
		elif sys.argv[i] == "--select-index":
			i += 1
			if i >= m:
				usage()
			select_index += parse_index(sys.argv[i])
		elif sys.argv[i] == "--exclude-index":
			i += 1
			if i >= m:
				usage()
			exclude_index += parse_index(sys.argv[i])
		elif sys.argv[i] == "--select-post":
			i += 1
			if i >= m:
				usage()
			select_post.append(sys.argv[i])
		elif sys.argv[i] == "--exclude-post":
			i += 1
			if i >= m:
				usage()
			exclude_post.append(sys.argv[i])
		elif sys.argv[i] == "--dry-run":
			dry_run = True
		elif sys.argv[i] == "--post-path":
			i += 1
			if i >= m:
				usage()
			post_path = sys.argv[i]
		elif sys.argv[i] == "--image-path":
			i += 1
			if i >= m:
				usage()
			image_path = sys.argv[i]
		else:
			usage()

		i += 1

	if i >= m:
		usage()

	# parse command
	if sys.argv[i] == "search-image":
		i += 1
		if i < m:
			select_image.append(sys.argv[i])
		search_image_in_posts(select_image, exclude_image, select_post, exclude_post, post_path)
	elif sys.argv[i] == "list-image":
		i += 1
		if i >= m:
			usage()
		list_image_in_one_post(select_image, exclude_image, select_index, exclude_index, sys.argv[i])
	elif sys.argv[i] == "rename-image":
		i += 2
		if i >= m:
			usage()
		rename_images(post_path, image_path, [[sys.argv[i-1], sys.argv[i]]], dry_run)
	elif sys.argv[i] == "batch-rename":
		i += 1
		if i >= m:
			usage()
		i += 1
		dest_pattern = sys.argv[i] if i < m else "{date}/{date2}_%03d"
		images = get_rename_image_list_in_one_post(dest_pattern, select_image, exclude_image, select_index, exclude_index, sys.argv[i-1])
		rename_images(post_path, image_path, images, dry_run)
	elif sys.argv[i] == "batch-rename-mult":
		i += 1
		if i >= m:
			usage()
		i += 1
		dest_pattern = sys.argv[i] if i < m else "{date}/{date2}_%03d"
		select_post.append(sys.argv[i-1])
		images = get_rename_image_list_in_posts(dest_pattern, select_image, exclude_image, select_post, exclude_post, post_path)
		rename_images(post_path, image_path, images, dry_run)
	elif sys.argv[i] == "list-unused-images":
		list_unused_images(select_image, exclude_image, select_post, exclude_post, post_path, image_path)
	elif sys.argv[i] == "list-duplicated-images":
		list_duplicated_images(select_image, exclude_image, select_post, exclude_post, post_path, image_path)
	else:
		usage()

if __name__ == '__main__':
	main()
