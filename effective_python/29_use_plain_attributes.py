import collections
import json
import os


class DatasetMeta(object):
    def __init__(self, meta_file):
        self._meta_file = meta_file
        self._meta = None
        self._meta_cls = None

    @property
    def meta(self):
        if self._meta is None:
            if not os.path.exists(self._meta_file):
                self._meta = {}
            else:
                with open(self._meta_file) as fin:
                    self._meta = json.load(fin)
        return self._meta

    @property
    def metacls(self):
        if self._meta_cls is None:
            obj_hook = lambda d: collections.namedtuple('config', d.keys())(*d.values())
            if os.path.exists(self._meta_file):
                with open(self._meta_file) as fin:
                    self._meta_cls = json.loads(fin.read(), object_hook=obj_hook)
            else:
                self._meta_cls = json.loads("{}", object_hook=obj_hook)
        return self._meta_cls

    @meta.setter
    def meta(self, new_meta):
        meta = self.meta
        override_keys = [k for k, v in meta.iteritems() if k in new_meta]
        if override_keys:
            print("Warning: The following keys will be override: %s." % json.dumps(override_keys))
        meta.update(new_meta)
        with open(self._meta_file, "w") as fout:
            json.dump(meta, fout)
        self._meta = meta

    def flush(self):
        self._meta = None
        if os.path.exists(self._meta_file):
            os.remove(self._meta_file)


if __name__ == '__main__':
    dataset_meta = DatasetMeta("a6.json")
    # print dataset_meta.meta
    # dataset_meta.meta = {"c": 7}
    # # dataset_meta.meta = {"a": 9}
    # print dataset_meta.meta
    print dataset_meta.metacls


