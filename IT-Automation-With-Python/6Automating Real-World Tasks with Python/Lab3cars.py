"""Original
Using a JSON file it calculates the car model with the most revenue (price * total_sales).
"""
#!/usr/bin/env python3

import json
import locale
import sys


def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  with open(filename) as json_file:
    data = json.load(json_file)
  return data


def format_car(car):
  """Given a car dictionary, returns a nicely formatted name."""
  return "{} {} ({})".format(
      car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
  """Analyzes the data, looking for maximums.

  Returns a list of lines that summarize the information.
  """
  max_revenue = {"revenue": 0}
  for item in data:
    # Calculate the revenue generated by this model (price * total_sales)
    # We need to convert the price from "$1234.56" to 1234.56
    item_price = locale.atof(item["price"].strip("$"))
    item_revenue = item["total_sales"] * item_price
    if item_revenue > max_revenue["revenue"]:
      item["revenue"] = item_revenue
      max_revenue = item
    # TODO: also handle max sales
    # TODO: also handle most popular car_year

  summary = [
    "The {} generated the most revenue: ${}".format(
      format_car(max_revenue["car"]), max_revenue["revenue"]),
  ]

  return summary



"""Fixed"""
#!/usr/bin/env python3

import json
import locale
import sys


def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  with open(filename) as json_file:
    data = json.load(json_file)
  return data


def format_car(car):
  """Given a car dictionary, returns a nicely formatted name."""
  return "{} {} ({})".format(
      car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
  """Analyzes the data, looking for maximums.

  Returns a list of lines that summarize the information.
  """
  max_revenue = {"revenue": 0}
  for item in data:
    # Calculate the revenue generated by this model (price * total_sales)
    # We need to convert the price from "$1234.56" to 1234.56
    item_price = locale.atof(item["price"].strip("$"))
    item_revenue = item["total_sales"] * item_price
    if item_revenue > max_revenue["revenue"]:
      item["revenue"] = item_revenue
      max_revenue = item
    # TODO: also handle max sales
    if item["total_sales"] > max_sales["total_sales"]:
      max_sales = item
    # TODO: also handle most popular car_year
    calculate_sales_per_year(item["car"],item["total_sales"])

  summary = [
    "The {} generated the most revenue: ${}".format(
      format_car(max_revenue["car"]), max_revenue["revenue"]),
    "The {} had the most sales: {}".format(
      format_car(max_sales["car"]), max_sales["total_sales"]),
      returns_most_popular_car_year()
  ]

  return summary

def cars_dict_to_table(car_data):
  """Turns the data in car_data into a list of lists."""
  table_data = [["ID", "Car", "Price", "Total Sales"]]
  for item in car_data:
    table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
  return table_data

def pdf_generator(summary,data):
  table_data=cars_dict_to_table(data)
  result=''
  for line in summary:
    result=result+line+'<br/>'
  reports.generate("/tmp/reportCars.pdf", "Sales Summary for last month",result,table_data )


def email_send_report(summary):
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  subject = "Sales summary for last month"
  body = '\n'.join(summary)
  message = emails.generate(sender, receiver, subject, body, "/tmp/reportCars.pdf")
  emails.send(message)

def main(argv):
  """Process the JSON data and generate a full report out of it."""
  data = load_data("/home/student-00-f525c13b1a30/car_sales.json")
  summary = process_data(data)
  # TODO: turn this into a pdf report
  pdf_generator(summary,data)
  # TODO: send the pdf report as an email attachment
  email_send_report(summary)

if __name__ == "__main__":
  main(sys.argv)
