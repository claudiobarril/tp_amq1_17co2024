import numpy as np
import pandas as pd
import re


def standardize_torque(torque_str):
    if pd.isna(torque_str):
        return np.nan

    # Match the torque value, unit, and RPM value
    torque_match = re.findall(r"(\d*\.?\d+)\s*(kgm|Nm|nm)?\s*@\s*([-\d\s,]*)\s*(rpm)?", torque_str)

    # If a match is found, process the first match
    if torque_match:
        value, unit, rpm_range, _ = torque_match[0]
        value = float(value)

        # Check for kgm and convert to Nm
        if 'kgm' in torque_str:
            value = value * 9.81  # Convert kgm to Nm

        # Format torque value to 2 decimal places
        torque_value = f"{value:.2f}Nm"

        # Clean and format the rpm_range
        rpm_value = rpm_range.strip().replace(',', '')  # Remove commas and whitespace

        # Combine torque and RPM value
        if rpm_value:
            return f"{torque_value} {rpm_value}rpm"
        else:
            return torque_value  # Return only the torque value if no RPM is found

    # Alternative regex to check for kgm in parentheses
    torque_match_alt = re.findall(r"(\d*\.?\d+)\s*@\s*([-\d\s,]*)\s*\(kgm@\s*rpm\)", torque_str)

    if torque_match_alt:
        value, rpm_range = torque_match_alt[0]
        value = float(value) * 9.81  # Convert kgm to Nm

        # Format torque value to 2 decimal places
        torque_value = f"{value:.2f}Nm"
        rpm_value = rpm_range.strip().replace(',', '')  # Remove commas and whitespace

        return f"{torque_value} {rpm_value}rpm"

    # Check for alternative formats (e.g., kgm without @)
    torque_match_kgm = re.findall(r"(\d*\.?\d+)\s*kgm\s*at\s*([-\d\s,]*)\s*(rpm)?", torque_str)

    if torque_match_kgm:
        value, rpm_range, _ = torque_match_kgm[0]
        value = float(value) * 9.81  # Convert kgm to Nm

        # Format torque value to 2 decimal places
        torque_value = f"{value:.2f}Nm"
        rpm_value = rpm_range.strip().replace(',', '')  # Remove commas and whitespace

        # Combine torque and RPM value
        if rpm_value:
            return f"{torque_value} {rpm_value}rpm"
        else:
            return torque_value  # Return only the torque value if no RPM is found

    # If no valid torque value is found, return NaN
    return np.nan


if __name__ == "__main__":
    # Sample data for testing
    torque_samples = [
        "190Nm@ 2000rpm",
        "250Nm@ 1500-2500rpm",
        "12.7@ 2,700(kgm@ rpm)",
        "22.4 kgm at 1750-2750rpm",
        "11.5@ 4,500(kgm@ rpm)",
        "113.75nm@ 4000rpm",
        "7.8@ 4,500(kgm@ rpm)",
        "59Nm@ 2500rpm",
        "170Nm@ 1800-2400rpm",
        "160Nm@ 2000rpm"
    ]

    # Create a DataFrame for testing
    car_details_v3 = pd.DataFrame({'torque': torque_samples})

    # Apply the function to standardize the torque values
    car_details_v3['torque_standardized'] = car_details_v3['torque'].apply(standardize_torque)

    # Display the DataFrame with standardized torque
    print(car_details_v3)
