import ditto_backend

print("RUNNING TEST...\n")

print("Current test: get_user_dir_path(1)")
print(ditto_backend.get_user_dir_path(1) + "\n")

print("Current test: creating libraries for user 1")
print(ditto_backend.create_lib(1, "dogs"))
print(ditto_backend.create_lib(1, "cats"))
print(ditto_backend.create_lib(1, "bats"))

print("Current test: get_user_dir_path(4)")
print(ditto_backend.get_user_dir_path(4) + "\n")

print("Current test: get_user_libs(1) Expected: Valid Output")
print(ditto_backend.get_user_libs(1))

print("Current test: get_user_libs(3)")
print(ditto_backend.get_user_libs(3))

print("Testing Library Creation")
print(ditto_backend.create_lib(4, "dogs"))