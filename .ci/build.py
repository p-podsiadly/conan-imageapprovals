import yaml
import subprocess

class Conan:

    @staticmethod
    def create(path, reference):
        res = subprocess.run(["conan", "create", path, reference])
        res.check_returncode()

with open("config.yml") as f:
    config = yaml.load(f, Loader=yaml.SafeLoader)
    for version, subdir in config["versions"].items():
        Conan.create(subdir, "{}@ppodsiadly/stable".format(version))
