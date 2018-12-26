
def pagination(total_count, current_page, per_page, base_url):
    total_number_of_pg_num = 20
    page_num_aplha = 10
    if not total_count: return []
    total_pages = int(total_count / per_page) + 1
    page_list = []
    for i in range(1, (total_pages + 1)):
        page_list.append({
            "url"       : base_url,
            "num"       : i,
            "active"    : False
        })

    if len(page_list) < total_number_of_pg_num:
        return page_list

    final_list = {
        "pre"   : { },
        "pages" : [ ],
        "next"  : { }
    }

    for i in page_list:
        min = (current_page-page_num_aplha)
        max = (current_page+page_num_aplha)
        if i["num"] > min and i["num"] < max:
            active = False
            if (current_page + 1) == i["num"]:
                active = True
            final_list["pages"].append({
                "url" : base_url + "&page=" + str(i["num"]),
                "num" : i["num"],
                "active" : active
            })

    return final_list
