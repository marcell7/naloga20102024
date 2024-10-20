import argparse
import os
import time


def permission_apply(
    root: str,
    depth: int,
    permission: str,
):
    """
    Recurively apply permission to all directories in root up to a specified depth.
    root: str - root directory
    depth: int - recursive depth
    permission: str - permission to apply
    """
    permission_code = int(permission, 8)
    curr_dirs = os.listdir(root)
    os.chmod(root, permission_code)

    if depth > 0:
        for dir_ in curr_dirs:
            dir_path = os.path.join(root, dir_)
            if os.path.isdir(dir_path):
                os.chmod(dir_path, permission_code)
                permission_apply(dir_path, depth=depth - 1, permission=permission)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=str, default="/opt/dir1")
    parser.add_argument("--depth", type=int, default=3)
    parser.add_argument("--permission", type=str, default="776")
    args = parser.parse_args()

    while True:
        try:
            permission_apply(args.root, args.depth, args.permission)
            print(f"{time.time()} -> Success", flush=True)
        except Exception as e:
            print(f"err: {e}", flush=True)

        time.sleep(5 * 60)
