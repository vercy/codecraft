import uuid

mapping_db = dict()


def store(content, content_key):
    print(f'store {content_key} -> {content}')


# class UpsertResult:
#     def __init__(self, key, is_new):
#         self.key = key
#         self.is_new = is_new
#
#
# def upsert(content_hash):
#     if content_hash in mapping_db:
#         return UpsertResult(mapping_db[content_hash], False)
#
#     new_key = uuid.uuid4()
#     mapping_db[content_hash] = new_key
#     return UpsertResult(new_key, True)


def upsert(content_hash):
    if content_hash in mapping_db:
        return mapping_db[content_hash], False

    new_key = uuid.uuid4()
    mapping_db[content_hash] = new_key
    return new_key, True


def get_content_key(content):
    content_hash = hash(content)
    key, is_new = upsert(content_hash)
    if is_new:
        store(content, key)

    return key


store_key = get_content_key('content1')
print(f'key: {store_key}')

store_key = get_content_key('content1')
print(f'key: {store_key}')

store_key = get_content_key('content2')
print(f'key: {store_key}')
