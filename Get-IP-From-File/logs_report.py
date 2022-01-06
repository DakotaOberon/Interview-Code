import sys

class LogsReport:
    def get_logs(self, *args):
        '''Retrieve data for ips based on date, hour, and status'''
        try:
            # Set variables to args, removing extra arguments
            date, hour, status = args[0:3]
        except ValueError:
            # Let user know what they are missing
            print(f'Missing {3 - len(args)} argument(s)')
            print('Command is in the format of "logs_report {date} {hour} {status_code}')
            return

        # Create empty dictionary object to store ips
        reports = {}

        with open("log_file", "r") as log_file:
            # Read each line in the log file
            for x in log_file.read().splitlines():
                # Grab the values of each piece of info within the line
                timestamp, ip, code = x.split(' ')

                # Check if the line is what the user is looking for
                if timestamp.startswith(f'{date}T{hour}') and code == status:
                    # Increment the number of reports found for the ip
                    if ip in reports:
                        reports[ip] += 1
                    else:
                        reports[ip] = 1

        return self.format_output(reports)

    def format_output(self, _obj):
        '''Format reports object into a string to be displayed to console'''

        # Set default for longest key
        longest_key = 0

        if len(_obj):
            longest_key = len(max(_obj, key=len)) # Taken from https://stackoverflow.com/questions/10895567/find-longest-string-key-in-dictionary

        # Get spaces to be placed between header keys
        space_between = ' ' * longest_key

        # Create header string
        header = f'IP {space_between} Found\n'

        # Create underline filler string
        underline = ('-' * len(header)) + '\n'

        # Set default of report string
        r_string = ''

        # Append values to report string based on report object
        for key in _obj:
            spaces = ' ' * (longest_key - len(key))
            r_string += f'{key}{spaces}  |   {_obj[key]}\n' + underline

        return header + underline + r_string

def main():
    reporter = LogsReport()

    report_return = reporter.get_logs(*sys.argv[1:])

    if report_return:
        print(report_return)

if __name__ == '__main__':
    main()
