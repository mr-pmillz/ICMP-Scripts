#!/usr/bin/env python3

import time
import argparse


def calculate_transmission_time(transmit_value, rtt_ms):
    # Get the current Unix time in milliseconds
    current_epoch_ms = int(time.time() * 1000)

    # Calculate the ICMP timestamp difference
    transmission_time_ms = transmit_value - (rtt_ms / 2)

    # Calculate the transmission Unix timestamp
    transmission_unix_timestamp_ms = current_epoch_ms - transmission_time_ms

    # Convert milliseconds to seconds for time.gmtime()
    transmission_unix_timestamp_s = transmission_unix_timestamp_ms / 1000

    # Convert to human-readable format
    transmission_time_human = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(transmission_unix_timestamp_s))

    return transmission_time_human


def main():
    parser = argparse.ArgumentParser(description='Calculate remote server time based on ICMP timestamp and RTT.')
    parser.add_argument('--transmit', type=int, required=True, help='ICMP transmit value')
    parser.add_argument('--rtt', type=float, required=True, help='Round Trip Time in milliseconds')

    args = parser.parse_args()
    result = calculate_transmission_time(args.transmit, args.rtt)
    print(f"Remote Server time: {result}")


if __name__ == "__main__":
    main()
