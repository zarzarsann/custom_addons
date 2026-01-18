# -*- coding: utf-8 -*-
import json
from odoo import http, _
from odoo.http import request
from odoo.http import Response
import requests
from datetime import datetime, timedelta
from passlib.context import CryptContext
from werkzeug.security import check_password_hash, generate_password_hash
import hmac
from hashlib import pbkdf2_hmac
import base64
from io import BytesIO
from PIL import Image
import tempfile

from random import choice
import string
from urllib.parse import urlparse
from urllib.parse import parse_qs

class MyController(http.Controller):

    @http.route('/api/res_country', auth='none', methods=['GET'], csrf=False)
    def get_res_country(self):
        data = {}
        headers_json = {'Content-Type': 'application/json'}
        country = request.env['res.country'].sudo().search([('name', 'ilike', 'Myanmar')], limit=1)
        data = {
            'id': country.id,
            'name': country.name,
            'code': country.code
        }
        return Response(json.dumps(data), headers=headers_json)

    @http.route('/api/res_state', auth='none', methods=['GET'], csrf=False)
    def get_res_state(self):
        data = []
        headers_json = {'Content-Type': 'application/json'}
        country = request.env['res.country'].sudo().search([('name', 'ilike', 'Myanmar')], limit=1)
        states = request.env['res.country.state'].sudo().search([('country_id', '=', country.id)])
        for state in states:
            data.append({
                'id': state.id,
                'name': state.name,
                'code': state.code,
                'country_id': state.country_id.id
            })
        return Response(json.dumps(data), headers=headers_json)

    @http.route('/api/res_partner', auth='none', methods=['GET'], csrf=False)
    def get_res_partner(self):
        data = []
        headers_json = {'Content-Type': 'application/json'}
        partner = request.env['res.partner'].sudo().search([])
        for par in partner:
            data.append({
                'name': par.name,
                'email': par.email,
                'phone': par.phone
            })
        return Response(json.dumps(data), headers=headers_json)

    # Testing for POST API
    @http.route('/api/v1/res_partner', auth='none', methods=['POST'], csrf=False)
    def get_create_partner(self):
        # import pdb
        # pdb.set_trace()
        headers_json = {'Content-Type': 'application/json'}
        datas = json.loads(http.request.httprequest.data)
        res_partner = {
            'name': datas['name'],
            'email': datas['email'],
            'phone': datas['phone'],
        }
        partner = request.env['res.partner'].sudo().create(res_partner)
        if partner:
            data = {
                "success": True
            }
        return Response(json.dumps(data), headers=headers_json)

    @http.route('/api/delete_user', auth='none', methods=['POST'], csrf=False)
    def get_delete_user(self, **rec):
        headers_json = {'Content-Type': 'application/json'}
        datas = json.loads(http.request.httprequest.data)
        if datas['id']:
            id = datas['id']
            partner = request.env['res.partner'].sudo().browse(id)
            # user = request.env['res.users'].sudo().search([('partner_id', '=', partner.id)])
            # user.active = False
            partner.active = False
            data = {
                'success': True,
            }
        else:
            data = {
                'success': False,
            }
        return Response(json.dumps(data, indent=4, default=str), headers=headers_json)

    @http.route('/api/v1/generate_otp', auth='none', methods=['POST'], csrf=False)
    def get_generate_otp(self):
        data = []
        headers_json = {'Content-Type': 'application/json'}
        datas = json.loads(http.request.httprequest.data)
        otp = {
            'email': datas['email'],
            'phone_no': datas['phone_no'],
            'otp_code': datas['otp_code'],
            'active': datas['active']
        }
        generate_otp = request.env['generate.otp'].sudo().create(otp)
        if generate_otp:
            data = {
                "success": True
            }
        return Response(json.dumps(data), headers=headers_json)






