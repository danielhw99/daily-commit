def solution(data, ext, val_ext, sort_by):
    data_type = ["code", "date", "maximum", "remain"]
    idx = data_type.index(ext)
    sort_with = data_type.index(sort_by)

    filtered = [row for row in data if row[idx] < val_ext]

    filtered.sort(key=lambda x: x[sort_with])

    return filtered
