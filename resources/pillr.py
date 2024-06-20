from datetime import datetime

from flask import request, Response
from flask_apispec import MethodResource, doc, use_kwargs, marshal_with
from flask_restful import Resource

# from common.api_tools import token_required
from models.pillm import PillModel
from resources import app, api #, docs
from services.pillv import PillService

class PillResource(MethodResource, Resource):
    def get(self, pill_id: int):
        pill_model = PillService().get_pill_by_id(pill_id)
        if pill_model:
            return pill_model.serialize(), 200
        else:
            return {'error': f'Pill not found for id: {pill_id}'}, 404

    # def put(self, pill_id: int, **kwargs):
    #     try:
    #         grid = kwargs.get('grid', None)
    #         piece = kwargs.get('piece', None)
    #         time = kwargs.get('time', None)

    #         pill_model = PillModel(id=pill_id, grid=grid, piece=piece, time=time)
    #         pill_model = PillService().update_pill(pill_model)

    # #         return pill_model, 200
    # #     except Exception as error:
    # #         return {'error': f'{error}'}, 400
    def put(self, pill_id: int, **kwargs):
        try:
            updated_fields = {k: v for k, v in kwargs.items() if v is not None}
            if not updated_fields:
                return {'error': 'No fields provided for update'}, 400
            
            pill_model = PillService().update_pill(pill_id, **updated_fields)

            if pill_model:
                return pill_model.serialize(), 200
            else:
                return {'error': f'Pill not found for id: {pill_id}'}, 404
        except Exception as error:
            return {'error': str(error)}, 400
    # def put(self, pill_id: int, **kwargs):
    #     try:
    #         updated_pill = PillService().update_pill(pill_id, **kwargs)

    #         if updated_pill:
    #             return updated_pill.serialize(), 200
    #         else:
    #             return {'error': f'Pill not found for id: {pill_id}'}, 404
    #     except Exception as error:
    #         return {'error': f'(error)'}, 400
    def delete(self, pill_id: int):
        success = PillService().delete_pill_by_id(pill_id)
        if success:
            return {'message': f'Successfully deleted pill with id: {pill_id}'}, 204
        else:
            return {'error': f'Failed to delete pill with id: {pill_id}. Pill not found.'}, 404

class PillListResource(Resource):
    def get(self):
        pill_list = PillService().get_all_pills()
        return [pill_model.serialize() for pill_model in pill_list]

    # @token_required()Pill
    def post(self):
        try:
            request_json = request.json
            if request_json:
                grid = request_json.get('grid', None)
                piece = request_json.get('piece', None)
                time = datetime.fromisoformat(request_json.get('time', None))

                pill_model = PillModel(grid=grid, piece=piece, time=time)
                PillService().create_pill(pill_model)

                return pill_model.serialize(), 200
            else:
                return {'error': 'Please provide pill info as a json'}, 400
        except Exception as error:
            return {'error': f'{error}'}, 400
        


api.add_resource(PillResource,'/pills/<pill_id>')
api.add_resource(PillListResource, '/pills')

