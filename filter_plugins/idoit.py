#!/usr/bin/python


class FilterModule(object):
    def filters(self):
        return {"updatepath": self.update_path}

    def update_path(self, matrix, current_version, desired_version):
        current_version = int(current_version)
        desired_version = int(desired_version)
        path = []
        for version, requirements in matrix.items():
            if version == desired_version:
                path.append(version)
                return path
            if version <= current_version or requirements["can_skip_update"]:
                continue
            path.append(version)
        return path
