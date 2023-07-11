dict_ = dict()
while True:
    key_val = input().split()
    if len(key_val) > 1:
        dict_.update([key_val])
    else:
        key_val == ''
        break
key_val1 = input()
print()
for k, v in dict_.items():
    if key_val1 == v:
        print(k)
        break
else:
    v != dict_
    print('! value error !')

# 1004 ER_CANT_CREATE_FILE
# 1005 ER_CANT_CREATE_TABLE
# 1006 ER_CANT_CREATE_DB
# 1007 ER_DB_CREATE_EXISTS

# ER_CANT_CREATE_TABLE

# 1005

# 4107 ER_SRS_UNUSED_PROJ_PARAMETER_PRESENT
# 4108 ER_GIPK_COLUMN_EXISTS
# 4111 ER_DROP_PK_COLUMN_TO_DROP_GIPK
# 4113 ER_DA_EXPIRE_LOGS_DAYS_IGNORED

# ER_DB_CREATE_EXISTS

# ! value error !