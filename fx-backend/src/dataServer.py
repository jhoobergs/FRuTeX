#!/usr/bin/env python3
from apiserver import ApiServer, ApiRoute, ApiError
from project import Project

p = Project()
p.parse()

class MyServer(ApiServer):
        @ApiRoute("/data")
        def getData(req):
            return p.generate_json()
            #return {"boo":req["bar"]+1}

        @ApiRoute("/update")
        def amend(req): # Cell pos, attribute and new expression
            return p.update_expression((req["row"], req["col"]), req["attrib"], req["expr"])            

        @ApiRoute("/baz")
        def justret(req):
            if req:
                 raise ApiError(501,"no data in for baz")
            return {"obj":1}


MyServer("127.0.0.1",8000).serve_forever()