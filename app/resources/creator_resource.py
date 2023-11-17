from flask_restful import Resource, reqparse, request


creator_parser = reqparse.RequestParser()
creator_parser.add_argument('lang', type=str, help='زبان انتخاب نشده',required=True)
creator_parser.add_argument('dispalyName', type=str, help='نام را وارد کنید',required=True)
creator_parser.add_argument('persianName', type=str, help='نام را وارد کنید',required=False)
creator_parser.add_argument('keywords',action='append',type=str, required=True, help='کلیدواژه انتخاب نشده')
creator_parser.add_argument('jobs',action='append',type=str, required=True, help='دسته بندی انتخاب نشده')
creator_parser.add_argument('classLogo',action='append',type=str, required=True, help='نوع لوگو انتخاب نشده')
creator_parser.add_argument('pallet',type=str, required=True, help='پالت انتخاب نشده')


class creator_resource(Resource):
    def post(self):
        args = creator_parser.parse_args()
        print(args)
        return True
