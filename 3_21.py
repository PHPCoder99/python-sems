dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
result_set = set()

for i in dict:
    for j in i:
        result_set.add(i[j])

print(result_set)