from os import listdir, path as os_path, access, R_OK, W_OK, walk

class vormise:
    def __init__(self, Path):
        self.tar_path = Path

        self.dirs = list()
        self.files = list()

        self.dirs_len = 0
        self.files_len = 0

        self.forbidden_dirs_len = 0
        self.forbidden_files_len = 0

        self.traverse(self.tar_path)

    def check_access_lvl(self, Path):
        return (False, False) if not os_path.exists(Path) else (access(Path, R_OK), access(Path, W_OK))

    def traverse(self, Path):
        for dir_path, dir_names, file_names in walk(self.tar_path):
            item_names = dir_names + file_names

            for item_name in item_names:
                abs_path = os_path.join(dir_path, item_name)
                vars = [self.dirs_len, self.files_len] if self.check_access_lvl(abs_path) == (True, True) else [self.forbidden_dirs_len, self.forbidden_files_len]

                if os_path.isfile(abs_path):
                    vars[1] += 1
                    self.files.append(abs_path)

                elif os_path.isdir(abs_path):
                    vars[0] += 1
                    self.dirs.append(abs_path)


