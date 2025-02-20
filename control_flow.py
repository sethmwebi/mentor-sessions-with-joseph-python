# num = -45
#
# if num > 50:
#     print("Positive")
# elif num > 25:
#     print("Greater than 25")
# else:
#     print("Negative")
def pass_fail(score):
    return "pass" if score >= 50 else "fail"
    # js
    # return score >= 50 ? "pass" : "fail"

print(pass_fail(49))
