import csv
import re
from collections import Counter
from flask import Flask, render_template, request

app = Flask(__name__)


def parse(data):
    pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    ips = re.findall(pattern, data)
    results_full = Counter(ips)
    results = results_full.most_common(20)
    return results_full, results


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        log = request.files['log_file'].read()
        txt = str(log, 'utf8')
#        result = parse(txt)
        result_full, result = parse(txt)
        ban = []
        for key, value in result:
            if value > 100:
                ban.append({'ip': key, 'counts': value})

        with open('output.csv', mode='w') as csvfile:
            writer = csv.writer(csvfile)
            header = ['IP', 'Frequency']
            writer.writerow(header)
            for item in result_full:
                writer.writerow((item, result_full[item]))

        return render_template('index.html', ips=ban)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
