import os
import shutil
import time

def main():

	deleted_folders_count = 0
	deleted_files_count = 0

	path = "/PATH_TO_DELETE"

	days = 30

	seconds = time.time() - (days * 24 * 60 * 60)

	if os.path.exists(path):

		for root_folder, folders, files in os.walk(path):

			if seconds >= get_file_or_folder_age(root_folder):

				remove_folder(root_folder)
				deleted_folders_count += 1 

				break

			else:

				for folder in folders:

					folder_path = os.path.join(root_folder, folder)

					if seconds >= get_file_or_folder_age(folder_path):

						remove_folder(folder_path)
						deleted_folders_count += 1 


				for file in files:

					file_path = os.path.join(root_folder, file)

					if seconds >= get_file_or_folder_age(file_path):

						remove_file(file_path)
						deleted_files_count += 1

		else:

			if seconds >= get_file_or_folder_age(path):

				remove_file(path)
				deleted_files_count += 1

	else:

		# file/folder is not found
		print(f'"{path}" is not found')
		deleted_files_count += 1

	print(f"Total folders deleted: {deleted_folders_count}")
	print(f"Total files deleted: {deleted_files_count}")


def remove_folder(path):

	# removing the folder
	if not shutil.rmtree(path):

		print(f"{path} is removed successfully")

	else:

		print(f"Unable to delete the "+path)



def remove_file(path):

	if not os.remove(path):

		print(f"{path} is removed successfully")

	else:

		# failure message
		print("Unable to delete the "+path)


def get_file_or_folder_age(path):

	# getting ctime of the file/folder
	# time will be in seconds
	ctime = os.stat(path).st_ctime

	# returning the time
	return ctime


if __name__ == '__main__':
	main()
