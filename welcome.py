import json
import os

from lib.strings import Strings
from lib.colors import ANSIColors
from lib.fsutils import DirectoryFilters, FileFilters

s_welcome = Strings.pad_spaces(f"{ANSIColors.GREEN}Welcome to yeppiidev's python projects!{ANSIColors.END}", 2)
m_lib_dir_list = os.listdir("lib")
m_lib_dir_list = DirectoryFilters.filter_python_autogen(m_lib_dir_list)

m_lib_info = json.loads(open("lib/libinfo.json", "r").read())

Strings.lines(f"{ANSIColors.BROWN}={ANSIColors.END}", len(s_welcome))
print(s_welcome)
Strings.lines(f"{ANSIColors.BROWN}={ANSIColors.END}", len(s_welcome))

print(f"\n{ANSIColors.LIGHT_CYAN}List of libraries available:{ANSIColors.END}")
for item in m_lib_dir_list:
    l_extstripped_item = FileFilters.remove_ext(item)
    
    try:
        l_item_type = m_lib_info['libs'][item]['type']
    except:
        l_item_type = 'Unknown?'
    
    print(f" ({l_item_type}) {ANSIColors.LIGHT_BLUE}{ANSIColors.BLINK}->{ANSIColors.END} {ANSIColors.YELLOW}{l_extstripped_item}{ANSIColors.END}: {m_lib_info['libs'][item]['desc']}")