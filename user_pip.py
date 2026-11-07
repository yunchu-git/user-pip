import subprocess
import ensurepip

def print_output (order,capture_output=True,text=True,shell=True):
    result = subprocess.run(order, capture_output=capture_output,text=text,shell=shell)
    print(result.stdout)
    if result.stderr:
        print(result.stderr)

def pip_install (python="python",pip="pip",mirror="https://pypi.tuna.tsinghua.edu.cn/simple"):
    ensurepip.bootstrap()
    print_output(f"{python} -m {pip} install -i {mirror} --upgrade pip")

def pip_upgrade (python="python",pip="pip",mirror="https://pypi.tuna.tsinghua.edu.cn/simple"):
    print_output(f"{python} -m {pip} install -i {mirror} --upgrade pip")

def install (name,pip="pip",mirror="https://pypi.tuna.tsinghua.edu.cn/simple"):
    print_output(f"{pip} install {name} -i {mirror}")

def install_version(name,version,pip="pip",mirror="https://pypi.tuna.tsinghua.edu.cn/simple"):
    print_output(f"{pip} install {name}=={version} -i {mirror}")

def install_whl(file_path,pip="pip"):
    print_output(f'{pip} install "{file_path}"')

def uninstall (name,confirm=False,pip="pip",):
    if confirm:
        if name == "pip":
            raise RuntimeError("2*000002")
        else:
            print_output(f"{pip} uninstall {name} -y")
    else:
        raise RuntimeError ("2*000001")

def upgrade (name,pip="pip",mirror="https://pypi.tuna.tsinghua.edu.cn/simple"):
    print_output(f"{pip} install {name} --upgrade -i {mirror}")

def pip_list (pip="pip"):
    print_output(f"{pip} list")

def pip_upgrade_list (pip="pip",mirror="https://pypi.tuna.tsinghua.edu.cn/simple"):
    print_output(f"{pip} list -o -i {mirror}")

def pip_check (pip="pip"):
    print_output(f"{pip} check")

def show_package (name,pip="pip"):
    print_output(f"{pip} show {name}")

def config_set (section,key,value,pip="pip"):
    print_output(f"{pip} config set {section}.{key} {value}")

def config_get (section,key,pip="pip"):
    print_output(f"{pip} config get {section}.{key}")

def config_unset (section,key,pip="pip"):
    print_output(f"{pip} config unset {section}.{key}")