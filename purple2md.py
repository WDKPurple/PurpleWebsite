#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os.path
import os
import io
from zipfile import ZipFile
import xml.parsers.expat


def usage():
	print("""Usage: %s <file>

Available commands:
  to be added

Available options:
  to be added""" % sys.argv[0])
	sys.exit(1)


def docx_xml2md(fin, fout, filedate2, img_dict):
	S = {
		"begin_content": False,
		"end_content": False,
		"title": u"",
		"author": u"",
		"last_bookmark": u"",
		"elems": [],
	}

	def new_p():
		return {"style": u"", "r": []}

	def new_r():
		return {"style": u"", "b": False, "i": False, "content": u""}

	def start_element(name, attrs):
		S["elems"].append(name)
		if name == "w:p":
			S["p"] = new_p()
		elif name == "w:r":
			S["r"] = new_r()
		elif name == "w:pStyle":
			if "w:val" in attrs:
				S["p"]["style"] = attrs["w:val"]
		elif name == "w:rStyle":
			if "w:val" in attrs:
				S["r"]["style"] = attrs["w:val"]
		elif name == "w:b":
			S["r"]["b"] = True
		elif name == "w:i":
			S["r"]["i"] = True
		elif name == "w:br":
			S["r"]["content"] += "<br>"
		elif name == "a:blip":
			if "r:embed" in attrs:
				img = attrs["r:embed"]
				if img in img_dict:
					S["r"]["content"] += "![img](https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/" + img_dict[img] + ")"
				else:
					print "Warning: image", img, "not found"
		elif name == "w:bookmarkStart":
			s = attrs["w:name"] if "w:name" in attrs else ""
			S["last_bookmark"] = s
			if s == "js_content":
				if not S["begin_content"]:
					S["begin_content"] = True
					fout.write("---\ntitle: \"")
					fout.write(S["title"].encode("utf-8"))
					fout.write("\"\ndate: ")
					fout.write(filedate2.encode("utf-8"))
					fout.write("\nauthors: [\"")
					fout.write(S["author"].encode("utf-8"))
					fout.write("\"]\n---\n\n")
			elif s == "js_toobar3":
				S["end_content"] = True
		elif name == "w:bookmarkEnd":
			S["last_bookmark"] = u""

	def end_element(name):
		S["elems"].pop()
		if name == "w:r":
			i = len(S["p"]["r"]) - 1
			if i >= 0 and S["p"]["r"][i]["b"] == S["r"]["b"] and S["p"]["r"][i]["i"] == S["r"]["i"]:
				S["p"]["r"][i]["content"] += S["r"]["content"]
			elif len(S["r"]["content"]) > 0:
				S["p"]["r"].append(S["r"])
			S["r"] = new_r()
		elif name == "w:p":
			if S["begin_content"] and not S["end_content"]:
				content = ""
				for r in S["p"]["r"]:
					if r["b"]:
						prefix = "_**" if r["i"] else "**"
						suffix = "**_" if r["i"] else "**"
					else:
						prefix = "_" if r["i"] else ""
						suffix = "_" if r["i"] else ""
					content += prefix + r["content"] + suffix
				fout.write(content.encode("utf-8"))
				fout.write("\n\n")

	def char_data(data):
		back = S["elems"][-1]
		if back == "w:t":
			if S["begin_content"]:
				S["r"]["content"] += data
			else:
				data = data.strip()
				if len(data) > 0:
					last_bookmark = S["last_bookmark"]
					if last_bookmark == "activity-name":
						S["title"] += data
					elif last_bookmark == "meta_content":
						S["author"] += data
		else:
			print "Warning: unexpected text", data, "in", back

	p = xml.parsers.expat.ParserCreate()
	p.returns_unicode = True

	p.StartElementHandler = start_element
	p.EndElementHandler = end_element
	p.CharacterDataHandler = char_data

	p.ParseFile(fin)


def main():
	if len(sys.argv) < 2:
		usage()

	filename = sys.argv[1]
	idx = filename.rfind(".")
	ext = filename[idx+1:] if idx >= 0 else ""
	if ext == "docx":
		pass
	else:
		print "File format '%s' is currently unsupported" % ext
		sys.exit(1)

	filedate = filename.replace("\\", "/")
	idx = filedate.rfind("/")
	filedate = filedate[idx+1:] if idx >= 0 else filedate
	filedate = filedate.replace("-", "").replace(".", "")
	filedate = filedate[:8] ## yyyymmdd
	filedate2 = filedate[:4] + "-" + filedate[4:6] + "-" + filedate[6:] # yyyy-mm-dd

	try:
		os.makedirs(filedate2)
	except:
		pass

	img_dict = {}

	with ZipFile(filename, "r") as zf:
		# extract images
		images = []
		for s in zf.namelist():
			if s.startswith("word/media/") and not s.endswith("/"):
				images.append(s)

		images.sort()

		img_index = 0
		for s in images:
			s2 = s
			idx = s2.rfind("/")
			s2 = s2[idx+1:] if idx >= 0 else s2
			idx = s2.rfind(".")
			imgext = s2[idx+1:] if idx >= 0 else "bin"
			s2 = s2[:idx] if idx >= 0 else s2

			img_index += 1
			s3 = filedate2 + "/" + filedate + ("_%03d." % img_index) + imgext
			img_dict[s2] = s3

			with zf.open(s, "r") as fin:
				with open(s3, "wb") as fout:
					fout.write(fin.read())

		# extract contents
		with zf.open("word/document.xml", "rU") as fin:
			with open(filedate2 + ".md", "w") as fout:
				docx_xml2md(fin, fout, filedate2, img_dict)


if __name__ == '__main__':
	main()
