import pickle

from flask import Flask, Markup, flash, jsonify, render_template, request

app = Flask(__name__)

log_model = None


with open("static/Encoded_dicts.pk1", "rb") as f:
    (
        category_dict,
        state_dict,
        roundA_dict,
        roundB_dict,
        roundC_dict,
        roundD_dict,
        investments_dict,
        top500_dict,
        vc_dict,
        rounds_dict,
    ) = pickle.load(f)


@app.route("/", methods=["POST", "GET"])
def index():
    global log_model, category_dict, state_dict

    with open("static/log_model.p", "rb") as f:
        log_model = pickle.load(f)

    return render_template(
        "index.html",
        category_dict=category_dict,
        state_dict=state_dict,
        roundA_dict=roundA_dict,
        roundB_dict=roundB_dict,
        roundC_dict=roundC_dict,
        roundD_dict=roundD_dict,
        investments_dict=investments_dict,
        top500_dict=top500_dict,
        vc_dict=vc_dict,
        rounds_dict=rounds_dict,
    )


@app.route("/background_process", methods=["POST", "GET"])
def background_process():
    with open("static/flask_df.pk1", "rb") as f:
        flask_df = pickle.load(f)
    with open("static/log_model.p", "rb") as f:
        log_model = pickle.load(f)

    Category = request.args.get("Category")
    State = request.args.get("State")
    Investments = request.args.get("Investments")
    Top500 = request.args.get("Top500")
    VC = request.args.get("VC")

    Funding_rounds = request.args.get("Funding_rounds")
    Founded_year = int(request.args.get("Founded_year"))
    print(Founded_year)
    First_Funding_Year = int(request.args.get("First_Funding_Year"))

    Total_Funding = int(request.args.get("Total_Funding")) * 100000
    Round_A = request.args.get("Round_A")
    Round_A_Amount = int(request.args.get("Round_A_Amount")) * 1000000
    Round_A_funded = int(request.args.get("Round_A_funded"))

    Round_B = request.args.get("Round_B")
    Round_B_Amount = int(request.args.get("Round_B_Amount")) * 100000
    Round_B_funded = int(request.args.get("Round_B_funded"))

    Round_C = request.args.get("RoundC")
    Round_C_Amount = int(request.args.get("Round_C_Amount")) * 100000
    Round_C_funded = int(request.args.get("Round_C_funded"))

    Round_D = request.args.get("Round_D_Amount")
    Round_D_Amount = int(request.args.get("Round_D_Amount")) * 100000
    Round_D_funded = int(request.args.get("Round_D_funded"))

    df = flask_df
    if Category != "Advertising":
        df["category_list_{}".format(category_dict[Category])] = 1

    if State != "CA":
        df["state_code{}".format(state_dict[State])] = 1

    age = 2020 - Founded_year
    if age < 4.5:
        df["age(-inf-4.5]"] = 1
    elif 4.5 < age < 7.5:
        df["age(4.5-7.5]"] = 1
    elif 7.5 < age < 12.5:
        df["age(7.5-12.5]"] = 1
    elif 12.5 < age:
        df["age(12.5-inf]"] = 1

    if Funding_rounds == "0" or Funding_rounds == "1":
        df["funding_rounds(-inf-1.5]"] = 1
    elif Funding_rounds == "2":
        df["funding_rounds(1.5-2.5]"] = 1
    elif Funding_rounds == "3":
        df["funding_rounds(2.5-3.5]"] = 1
    elif Funding_rounds == "More than 3":
        df["funding_rounds(2.5-3.5]"] = 1

    age_first_funding = First_Funding_Year - Founded_year
    if age_first_funding < 0.5:
        df["age_first_funding(-inf-0.5]"] = 1
    elif 0.5 < age_first_funding < 1.5:
        df["age_first_funding(0.5-1.5]"] = 1
    elif 1.5 < age_first_funding < 5.5:
        df["age_first_funding(1.5-5.5]"] = 1
    elif 5.5 < age_first_funding:
        df["age_first_funding(5.5-inf]"] = 1

    if Total_Funding <= 130000:
        df["funding_total_usd(-inf-130000]"] = 1
    elif 130000 < Total_Funding <= 1806473:
        df["funding_total_usd(130000-1806473]"] = 1
    elif 1806473 < Total_Funding <= 12200000:
        df["funding_total_usd(1806473-12200000]"] = 1
    elif 12200000 < Total_Funding:
        df["funding_total_usd(12200000-inf]"] = 1

    if Round_A_Amount <= 2573250:
        df["roundA_raised_amount(-inf-2573250]"] = 1
    elif 2573250 < Round_A_Amount <= 5000000:
        df["roundA_raised_amount(2573250-5000000]"] = 1
    elif 5000000 < Round_A_Amount <= 8434284:
        df["roundA_raised_amount(5000000-8434284]"] = 1
    elif 8434284 < Round_A_Amount:
        df["roundA_raised_amount(8434284-inf]"] = 1

    RoundA_age = Round_A_funded - Founded_year
    if RoundA_age < 1.5:
        df["roundA_age(-inf-1.5]"] = 1
    elif 1.5 < RoundA_age < 2.5:
        df["roundA_age(1.5-2.5]"] = 1
    elif 2.5 < RoundA_age < 3.5:
        df["roundA_age(2.5-3.5]"] = 1
    elif 3.5 < RoundA_age:
        df["roundA_age(3.5-inf]"] = 1

    RoundB_age = Round_B_funded - Founded_year
    if RoundB_age < 1.5:
        df["roundB_age(-inf-1.5]"] = 1
    elif 1.5 < RoundB_age < 2.5:
        df["roundB_age(1.5-2.5]"] = 1
    elif 2.5 < RoundB_age < 4.5:
        df["roundB_age(2.5-4.5]"] = 1
    elif 4.5 < RoundB_age:
        df["roundB_age(4.5-inf]"] = 1

    if Round_B_Amount <= 6000000:
        df["roundB_raised_amount(-inf-6000000]"] = 1
    elif 6000000 < Round_B_Amount <= 10000000:
        df["roundB_raised_amount(6000000-10000000]"] = 1
    elif 10000000 < Round_B_Amount <= 16999999:
        df["roundB_raised_amount(10000000-16999999]"] = 1
    elif 16999999 < Round_B_Amount:
        df["roundB_raised_amount(16999999-inf]"] = 1

    RoundC_age = Round_C_funded - Founded_year
    if RoundC_age < 2.5:
        df["roundC_age(-inf-2.5]"] = 1
    elif 2.5 < RoundC_age < 4.5:
        df["roundC_age(2.5-4.5]"] = 1
    elif 4.5 < RoundC_age < 6.5:
        df["roundC_age(4.5-6.5]"] = 1
    elif 6.5 < RoundC_age:
        df["roundC_age(6.5-inf]"] = 1

    if Round_C_Amount <= 8177499:
        df["roundC_raised_amount(-inf-8177499]"] = 1
    elif 8177499 < Round_C_Amount <= 14500000:
        df["roundC_raised_amount(8177499-14500000]"] = 1
    elif 14500000 < Round_C_Amount <= 24385000:
        df["roundC_raised_amount(14500000-24385000]"] = 1
    elif 24385000 < Round_C_Amount:
        df["roundC_raised_amount(24385000-inf]"] = 1

    RoundD_age = Round_D_funded - Founded_year
    if RoundD_age < 3.5:
        df["roundD_age(-inf-3.5]"] = 1
    elif 3.5 < RoundD_age < 5.5:
        df["roundD_age(3.5-5.5]"] = 1
    elif 5.5 < RoundD_age < 7.5:
        df["roundD_age(5.5-7.5]"] = 1
    elif 7.5 < RoundD_age:
        df["roundD_age(7.5-inf]"] = 1

    if Round_D_Amount <= 14608981:
        df["roundD_raised_amount(-inf-14608981]"] = 1
    elif 14608981 < Round_D_Amount <= 21051931:
        df["roundD_raised_amount(14608981-21051931]"] = 1
    elif 21051931 < Round_D_Amount <= 35168000:
        df["roundD_raised_amount(21051931-35168000]"] = 1
    elif 35168000 < Round_D_Amount:
        df["roundD_raised_amount(35168000-inf]"] = 1

    if Round_A == "Yes" and Round_A_Amount > 0.5:
        df["has_roundA"] = 1
    if Round_B == "Yes" and Round_B_Amount > 0.5:
        df["has_roundB"] = 1
    if Round_C == "Yes" and Round_C_Amount > 0.5:
        df["has_roundC"] = 1
    if Round_D == "Yes" and Round_D_Amount > 0.5:
        df["has_roundC"] = 1

    if Investments == 0 or Investments == 1:
        df["num_investments(-inf-1.5]"] = 1
    elif Investments == 2:
        df["num_investments(1.5-2.5]"] = 1
    elif Investments == 3:
        df["num_investments(2.5-4.5]"] = 1
    elif Investments == "More than 4":
        df["num_investments(4.5-inf]"] = 1
    elif Investments != "N/A":
        df["has_investors"] = 1

    if Top500 == 0:
        df["num_top500_investors(-inf-0.5]"] = 1
    elif Top500 == 1:
        df["num_top500_investors(0.5-1.5]"] = 1
    elif Top500 == 2:
        df["num_top500_investors(1.5-2.5]"] = 1
    elif Top500 == "More than 2":
        df["num_top500_investors(2.5-inf]"] = 1
    elif Top500 != "N/A":
        df["has_top500_investors"] = 1

    if VC != "N/A":
        df["vc"] = 1
    float_formatter = "{:.2f}".format
    output = float_formatter(log_model.predict_proba(df)[0][1] * 100)
    return jsonify({"pred": output})


if __name__ == "__main__":
    app.run(debug=True)
