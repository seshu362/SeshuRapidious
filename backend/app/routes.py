from flask import Blueprint, request, jsonify
from .opensearch_client import search_recipes

api_bp = Blueprint('api', __name__)

@api_bp.route('/search', methods=['GET'])
def search():
    keyword = request.args.get('q', '')
    filters = {
        "cuisine": request.args.get('cuisine', ''),
        "ingredients": request.args.get('ingredients', ''),
        "prep_time": request.args.get('prep_time', '')
    }
    page = int(request.args.get('page', 1))
    results_per_page = int(request.args.get('limit', 10))

    recipes = search_recipes(keyword, filters, page, results_per_page)
    return jsonify(recipes)
