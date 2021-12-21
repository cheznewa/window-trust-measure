import sys
import re
o = sys.stdin.read()
color="black"
if re.search("Browser",o) or re.search("brows",o) or re.search("Visited",o):
  color="yellow"
if re.search("Facebook",o) or re.search("Yahoo",o) or re.search("Google",o) or re.search("GitHub",o) or re.search("Microsoft",o):
  color="orange"
if re.search("Terminal",o) or re.search("DuckDuckGo",o):
  color="green"
if re.search("File",o) or re.search("Manager",o) or re.search("Calculator",o):
  color="black"
if re.search("Flash",o) or re.search("flash Player",o) or re.search("Ruffle",o):
  color="orange"
if re.search("hash",o) or re.search("Hash",o) or re.search("Checksum",o) or re.search("MD5",o) or re.search("SHA256",o):
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
if re.search("Network",o) or re.search("Connection",o):
  color="red"
if re.search("Info",o) or re.search("Information",o):
  color="blue"
if re.search("Confidential",o) or re.search("Top Secret",o) or re.search("Classified",o):
  color="red"
if re.search("Encrypted",o) or re.search("Secured",o) or re.search("Scrambled",o):
  color="black"

sys.stdout.write("%s\n" %(color))