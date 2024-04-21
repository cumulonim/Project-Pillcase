from datetime import datetime

from flask import request, Response
from flask_apispec import MethodResource, doc, use_kwargs, marshal_with
from flask_restful import Resource

from common.api_tools import token_required
from models.pillm import PillModel
from resources import app, api #, docs
from services.pillv import PillService

class PillResource(MethodResource, Resource):
    @doc(description="Get a pill's information", tags=['Pill Requests'])
    # @marshal_with(PillModelSchema, code=200)
    def get(self, pill_id: int):
        pill_model = PillService().get_pill_by_id(pill_id)
        if pill_model:
            return pill_model, 200
        else:
            return {'error': f'Pill not found for id: {pill_id}'}, 404

    @doc(description="Update a pill's information", tags=['Pill Requests'])
    # @use_kwargs(PillRequestSchema, location='json')
    # @use_kwargs(TokenSchema, location='headers')
    # @marshal_with(PillModelSchema, code=200)
    @token_required()
    def put(self, pill_id: int, **kwargs):
        try:
            grid = kwargs.get('name', None)
            piece = kwargs.get('piece', None)
            time = kwargs.get('time', None)

            pill_model = PillModel(id=pill_id, grid=grid, piece=piece, time=time)
            pill_model = PillService().update_pill(pill_model)

            return pill_model, 200
        except Exception as error:
            return {'error': f'{error}'}, 400


api.add_resource(PillResource,'/pills/<pill_id>')
# api.add_resource(PillListResource, '/pills')

