import os
from ..main import permission_apply


def test_permission_apply():
    expected_permission = "776"
    depth = 3
    root = "./tests/dir1"

    os.mkdir(root)
    paths = [
        "/dir1-1",
        "/dir1-1/dir1-1-1",
        "/dir1-1/dir1-1-1/dir1-1-1-1",
        "/dir1-1/dir1-1-1/dir1-1-1-1/dir1-1-1-1-1",
        "/dir1-1/dir1-1-2",
        "/dir1-2",
        "/dir1-2/dir1-2-1",
        "/dir1-2/dir1-2-1/dir1-2-1-1",
        "/dir1-2/dir1-2-1/dir1-2-1-1/dir1-2-1-1-1",
        "/dir1-3",
    ]
    for dir_ in paths:
        os.mkdir(f"{root}{dir_}")

    try:
        permission_apply(root, depth, expected_permission)
    except Exception as e:
        os.system(f"rm -rf {root}")
        assert False, f"err: {e}"

    for dir_ in [root, *paths]:
        dir_path = f"{root}{dir_}" if dir_ != root else root
        permission = oct(os.stat(dir_path).st_mode)[-3:]
        dir_name = dir_path.split("/")[-1]
        if dir_name == "dir1-1-1-1-1" or dir_name == "dir1-2-1-1-1":
            if permission != expected_permission:
                continue
            else:
                os.system(f"rm -rf {root}")
                assert (
                    False
                ), f"err: {dir_name} -> {permission} == {expected_permission}"

        if permission != expected_permission:
            os.system(f"rm -rf {root}")
            assert False, f"err: {dir_name} -> {permission} != {expected_permission}"

    os.system(f"rm -rf {root}")

    assert True
