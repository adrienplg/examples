import json
import requests
from datetime import datetime
from datetime import date

class MarketingSource(object):

    def __init__(self, name):
        self.name = name
        self.leads = []
        self.leases = []
        self.leads_per_quarter = dict() # {YYYY Qx: int}
        self.leases_per_quarter = dict() # {YYYY Qx: int}
        self.cost_per_quarter = dict() # {YYYY Qx: int}

    def __str__(self):
        return 'name: {}, leads: {}, leases: {}'.format(self.name, self.leads, self.leases)

    def __repr__(self):
        return '{}(name: {}, leads: {}, leases: {})'.format(self.__class__.__name__, self.name, self.leads, self.leases)


def load_leads(leads_list):
    """ Load information from the leads list
        Creates MarketingSource objects and add them to a list

        Args:

        Return:
    """

    marketing_sources = []

    for lead in leads_list:
        # Name of the marketing source
        json_msource_name = lead.get('marketing_source')

        # Marketing source name is not null
        if json_msource_name:
            #print(json_msource_name)
            # Extract relevant information
            lease_date = lead.get('lease_signed')
            lead_date = lead.get('first_seen')
            #print('lease_date: {}, lead_date: {}'.format(lease_date, lead_date))

            existing_market = False

            for market in marketing_sources:
                # MarketingSource is already a listed object
                if market.name == json_msource_name:
                    existing_market = True
                    if lease_date:
                        market.leases.append(lease_date)
                    market.leads.append(lead_date)
                    # No need to look for the remaining items in the list
                    break

            # New marketing source
            if not existing_market:
                new_market = MarketingSource(json_msource_name)
                if lease_date:
                    new_market.leases.append(lease_date)
                new_market.leads.append(lead_date)
                marketing_sources.append(new_market)

    return marketing_sources


def numbers_per_quarter(marketing_sources):
    """ Set the leases per quarter and leads per quarter for each marketing source """

    for msource in marketing_sources:
        for lead in msource.leads:
            date_object = datetime.strptime(lead, '%Y-%m-%d')
            quarter = (date_object.month-1)//3 + 1
            quarter_name = '{} Q{}'.format(str(date_object.year), quarter)
            try:
                msource.leads_per_quarter[quarter_name] += 1
            except KeyError:
                msource.leads_per_quarter[quarter_name] = 1

        for lease in msource.leases:
            date_object = datetime.strptime(lead, '%Y-%m-%d')
            quarter = (date_object.month-1)//3 + 1
            quarter_name = '{} Q{}'.format(str(date_object.year), quarter)
            try:
                msource.leases_per_quarter[quarter_name] += 1
            except KeyError:
                msource.leases_per_quarter[quarter_name] = 1

    return marketing_sources

def quarter_costs(marketing_sources):
    """ Calculate the cost per quarter of the different marketing sources. """

    for msource in marketing_sources:
        if msource.name == 'Apartment Guide':
            total_cost = 495 * 3
            for quarter in msource.leads_per_quarter.keys():
                msource.cost_per_quarter[quarter] = total_cost

        elif msource.name == 'Apartments.com':
            price_per_signed_lease = 295
            for quarter, number_of_leads in msource.leads_per_quarter.items():
                msource.cost_per_quarter[quarter] = price_per_signed_lease * number_of_leads

        elif msource.name == 'Rent.com':
            # TODO: missing the resident_rent
            price_per_signed_lease = 595
            for quarter, number_of_leases in msource.leases_per_quarter.items():
                msource.cost_per_quarter[quarter] = price_per_signed_lease * number_of_leases

        elif msource.name == 'For Rent':
            cost_per_month = 195
            price_per_lead = 25
            for quarter, number_of_leads in msource.leads_per_quarter.items():
                msource.cost_per_quarter[quarter] = cost_per_month * 3 + price_per_lead * number_of_leads

        elif msource.name == 'Craigslist.com':
            cost_per_month = 0
            for quarter, number_of_leads in msource.leads_per_quarter.items():
                msource.cost_per_quarter[quarter] = 0

        elif msource.name == 'Resident Referral':
            price_per_signed_lease = 500
            for quarter, number_of_leases in msource.leases_per_quarter.items():
                msource.cost_per_quarter[quarter] = price_per_signed_lease * number_of_leases

    return marketing_sources


def print_report(marketing_sources):
    """ Use a list of MarketingSource objects to print a quarterly report. """

    final_report = dict()

    for msource in marketing_sources:
        for quarter in msource.cost_per_quarter.keys():
            leads = msource.leads_per_quarter[quarter]
            try:
                leases = msource.leases_per_quarter[quarter]
            except KeyError:
                leases = 0
            cost = msource.cost_per_quarter[quarter]

            formatted_string = ('{} - total leads: {}, signed leases: {}, total cost: ${}, '
                                'avg cost per lead: ${}'.format(msource.name, leads, leases, cost, format(cost/leads, '.2f')))

            try:
                final_report[quarter].append(formatted_string)
            except KeyError:
                final_report[quarter] = [formatted_string]

    for quarter, items in final_report.items():
        print(quarter)
        for item in items:
            print(item)


def get_json_file(url):
    """ Get a JSON file from a given URL """

    response = requests.get(url)
    leads = json.loads(response.text)
    # Object returned by the URL is a list, therefore returning its content
    return leads


url = 'https://gist.githubusercontent.com/pplante/a2a4532d7125804dfbe4/raw/89d02a5d5d2aa7e2cb9ad968b4d58b6911915aa4/guest_cards.json'
#leads_file = get_json_file(url)
#marketing_list = load_leads(leads_file)
#marketing_list = numbers_per_quarter(marketing_list)
#marketing_list = quarter_costs(marketing_list)
#print_report(marketing_list)

my_date = date(2015, 2, 4)
begin = date(2015, 1, 1)
end = date(2015, 2, 5)
print(my_date)
is_valid = begin < my_date and my_date < end
print(is_valid)

