from flask import Flask, jsonify, request
import pandas as pd


app = Flask(__name__)


dfs = []
dfs.append(pd.read_csv("3.csv", encoding = "cp1251", sep=';', error_bad_lines=False).\
    rename(index=str, columns={'АВС/ DEF': "code", "Регион": "region", "От": "from", "До": "to"}))
dfs.append(pd.read_csv("4.csv", encoding = "cp1251", sep=';', error_bad_lines=False).\
    rename(index=str, columns={'АВС/ DEF': "code", "Регион": "region", "От": "from", "До": "to"}))
dfs.append(pd.read_csv("8.csv", encoding = "cp1251", sep=';', error_bad_lines=False).\
    rename(index=str, columns={'АВС/ DEF': "code", "Регион": "region", "От": "from", "До": "to"}))
dfs.append(pd.read_csv("9.csv", encoding = "cp1251", sep=';', error_bad_lines=False).\
    rename(index=str, columns={'АВС/ DEF': "code", "Регион": "region", "От": "from", "До": "to"}))


def get_region(df, phone):
    df_loc = df.loc[(df['code'] == int(phone[1:4])) & (df['from'] <= int(phone[4:])) & (df['to'] >= int(phone[4:]))]
    return df_loc.iloc[0].region.replace('г.', '').strip()


@app.route("/", methods=["GET"])
def api():
    if request.method == "GET":
        phone = request.args.get('phone')

        if int(phone[1]) == 3:
            return jsonify({'region': get_region(dfs[0], phone)})

        elif int(phone[1]) == 4:
            return jsonify({'region': get_region(dfs[1], phone)})

        elif int(phone[1]) == 8:
            return jsonify({'region': get_region(dfs[2], phone)})

        elif int(phone[1]) == 9:
            return jsonify({'region': get_region(dfs[3], phone)})
        else:
            return jsonify({'region': 'can not find region'})



if __name__ == '__main__':
    app.run()
