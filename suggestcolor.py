import sys
import re
o = sys.stdin.read()
color="black"
if re.search("Browser",o) or re.search("brows",o) or re.search("Visited",o):
  color="yellow"
if re.search("Facebook",o) or re.search("Yahoo",o) or re.search("Google",o) or re.search("GitHub",o) or re.search("Microsoft",o):
  color="orange"
if re.search("Terminal",o):
  color="green"
if re.search("File",o) or re.search("Manager",o) or re.search("Calculator",o):
  color="black"
if re.search("Flash",o) or re.search("flash Player",o) or re.search("Ruffle",o):
  color="orange"
if re.search("hash",o) or re.search("Hash",o) or re.search("Checksum",o):
  color="blue"
if re.search("debug",o) or re.search("Debug",o) or re.search("debugging",o):
  color="gray"
if re.search("VirtualBox",o) or re.search("Virtualization",o) or re.search("Virtual Machine",o):
  color="blue"
if re.search("porn",o) or re.search("Porn",o) or re.search("PoRn",o) or re.search("XXX",o):
  color="purple"
if re.search("virus",o) or re.search("Virus",o) or re.search("ViRu",o):
  color="red"
if re.search("Safe",o) or re.search("Trust",o) or re.search("trusted",o):
  color="green"


sys.stdout.write("%s\n" %(color))