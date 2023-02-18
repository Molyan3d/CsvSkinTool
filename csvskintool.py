import csv
import os

# Step 1: Look for skins.csv and skin_confs.csv in the same folder
cwd = os.getcwd()
skins_file = os.path.join(cwd, "skins.csv")
skin_confs_file = os.path.join(cwd, "skin_confs.csv")
# Step #: Check if file exist
if not os.path.isfile(skins_file) or not os.path.isfile(skin_confs_file):
    raise FileExistsError("Files not Found")

# Step #: Read file and defining some variables for use in future
with open(skins_file, mode='r', newline='') as file:
    skins_content = [row for row in csv.reader(file)]

with open(skin_confs_file, mode='r', newline='') as file:
    skin_confs_content = [row for row in csv.reader(file)]


skins_header = skins_content[0]
skin_confs_header = skin_confs_content[0]

# Skin confs definitions
skin_confs_character_column = skin_confs_header.index("Character")
skin_confs_model_column = skin_confs_header.index("Model")

# Skins definitions
skins_BlueTexture_column = skins_header.index("BlueTexture")
skins_RedTexture_column = skins_header.index("RedTexture")
skins_BlueSpecular_column = skins_header.index("BlueSpecular")
skins_RedSpecular_column = skins_header.index("RedSpecular")
skins_campaign_column = skins_header.index("Campaign")
skins_author_column = skins_header.index("CommunityCredit")
skins_tid_column = skins_header.index("TID")
skins_shoptid_column = skins_header.index("ShopTID")
skins_materials_column = skins_header.index("MaterialsFile")
material = ("max_geo.scw")

character_list = list(set([row[skin_confs_character_column] for i, row in enumerate(skin_confs_content) if i > 1 and row[skin_confs_character_column] != '']))

# credits
PACKAGE_VERSION = "\033[32m1.0\033[0m"
AUTHOR = "\033[32m@molyan_ & @Daniil-SV\033[0m"
GITHUB_LINK = "\033[32mgithub.com/Molyan3d/CsvSkinTool\033[0m"
COPYRIGHT_DESC = "\033[32m(c) Molyan Stars Team, 2023\033[0m"
def info(msg: str):
    print(f"\033[32m-> {msg}\033[0m")


def print_credits() -> None:
    print(f'\033[32mUltimate CSV Skin Tool - {PACKAGE_VERSION}\033[0m')
    info(f'\033[32mImplemented by {AUTHOR}\033[0m')
    info(GITHUB_LINK)
    info(COPYRIGHT_DESC)

#print credits
print_credits()


# Step #: Prompt the user to input the name of the skin
skin_name = input("Enter the name of the skin: ").upper()

# Step #: Prompt the user to input a code name for the skin
code_name = input("Enter the code name for the skin (Example: Pirate Carl -> WhirlwindPirate): ")

# Step #: Prompt the user to input the name of the skin file
skin_file_name = input("Enter the name of the skin file (Example: bo_geo.scw): ")

events = [
    "None",
    "Brawlidays",
    "Chinese New Year",
    "Brawl-o-ween",
    "Brown n friends",
    "Lunar New Year",
    "PSG",
    "Supercell Make",
    "Soon in the Archive",
    "Archive Skins",
    "Supercell 10 Years",
    "Brawl Pass Skins",
    "Welcome China",
    "Silver Skins",
    "Golden Skins"
]

# Prompt the user to choose an event
print("Choose an event:")
for key, value in enumerate(events):
    print(f"{key}: {value}")
event_choice = int(input("Enter the corresponding Event number: "))

# If the user chooses event 7, prompt the user to input the author/s of the skin
author = None
if event_choice == 7:
    author = input("Enter the Author/s of the skin: ")

# Prompt the user to input the texture name
texture_name = input("Enter the texture name (Example: bo_tex.png): ")

# Step #: Display the "Character" column content from "skin_confs.csv" file
for index, character in enumerate(character_list):
    print(f"{index}: {character}")

# Step #: Search for the first row containing the chosen name in "skin_confs.csv" file
chosen_character_index = int(input("Enter the number of the chosen character: "))
chosen_character = character_list[chosen_character_index]

for row in skin_confs_content:
    if row[skin_confs_character_column] == chosen_character:
        skin_confs_row = row

# Step 3: Create new rows empty row
skin_row = ["" for _ in range(len(skins_header))] # TODO

#Step #: Applying values to csv row

#Skin confs
skin_confs_row[0] = skin_name
skin_confs_row[skin_confs_model_column] = skin_file_name

# Skins
skin_row[0], skin_row[1] = (skin_name, skin_name)

if event_choice:
    skin_row[skins_campaign_column] = event_choice

    if author is not None:
        skin_row[skins_campaign_column] = event_choice
        skin_row[skins_author_column] = author

        if skin_file_name.endswith(".glb"):
            skin_row[skins_materials_column] = material

skin_row[skins_BlueTexture_column] = texture_name
skin_row[skins_RedTexture_column] = texture_name
skin_row[skins_BlueSpecular_column] = texture_name
skin_row[skins_RedSpecular_column] = texture_name
skin_row[skins_tid_column] = skin_name
skin_row[skins_shoptid_column] = skin_name



with open(skins_file, mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(skin_row)

with open(skin_confs_file, mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(skin_confs_row)

print(f"\033[1;32mThe files were saved successfully in {os.getcwd()}.\033[0m")

