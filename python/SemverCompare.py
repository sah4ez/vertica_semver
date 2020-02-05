import vertica_sdk


def versiontuple(v):
    return tuple(map(int, (v.split("."))))


class semver_compare(vertica_sdk.ScalarFunction):

    def processBlock(self, server_interface, arg_reader, res_writer):
        server_interface.log("Execute compare semver")
        while True:
            cur_version = arg_reader.getString(0)
            from_version = arg_reader.getString(1)
            to_version = arg_reader.getString(2)
            res_writer.setBool((versiontuple(from_version) <= versiontuple(cur_version)) and (versiontuple(cur_version) <= versiontuple(to_version)))
            res_writer.next()
            if not arg_reader.next():
                break

class semver_compare_factory(vertica_sdk.ScalarFunctionFactory):
    def getPrototype(self, srv_interface, arg_types, return_type):
        arg_types.addVarchar()
        arg_types.addVarchar()
        arg_types.addVarchar()
        return_type.addBool()
    def getReturnType(self, srv_interface, arg_types, return_type):
        return_type.addBool()
    def createScalarFunction(self, srv):
        return semver_compare()
