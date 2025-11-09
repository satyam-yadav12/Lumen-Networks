from flask import jsonify, request
from ..utils.db import (
    find_search_results_title,
    find_search_results_tags,
    find_total_count_of_results_title,
    find_total_count_of_results_tag,
    find_all_images,
)


# route("/search", methods=["GET"])
def search_keyword():
    keyword = request.args.get("q", "").strip()
    page = int(request.args.get("page", 1))
    limit = 10

    if not keyword:
        return jsonify({"error": "search keyword required"}), 400

    skip = (page - 1) * limit

    title_results = find_search_results_title(keyword, skip, limit)
    tag_results = find_search_results_tags(keyword, skip, limit)

    title_results = list(title_results)
    tag_results = list(tag_results)

    total_title = find_total_count_of_results_title(keyword)
    total_tag = find_total_count_of_results_tag(keyword)

    response = {
        "title_result": title_results,
        "tag_result": tag_results,
        "total_title": total_title,
        "total_tag": total_tag,
        "keyword": keyword,
    }

    return jsonify({"data": response, "response_code": 200}), 200


# route("/allimages", methods=["GET"])
def fetch_all_images():
    result, count = find_all_images()
    return jsonify({"result": result, "count": count})
