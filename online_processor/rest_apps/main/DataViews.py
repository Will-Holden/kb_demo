from . import inf_restful
from flask import Flask, request, jsonify
import json
from utils.Encoder import JSONEncoder
from services.LinkerService import linkerService
from services.DataService import dataService
from services.PaintService import paintService

# @inf_restful.route("/hellow", methods=['GET'])
# def hellow():
#     return "hellow"


@inf_restful.route('/online/paint',
                   methods=["POST"])
def paint_cv():
    """
    statistic and visualize a cv by diagram
    :return: json format
    """
    if request.method == 'POST':
        cv_id = request.form["_id"]
        paint_result = paintService.paint_cv(cv_id)
        return json.dumps(paint_result,ensure_ascii=False,cls=JSONEncoder)

