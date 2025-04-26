import streamlit as st

def convert_units(value, unit_from, unit_to):
    conversion = {
        'meters_kilometers': 0.001,
        'kilometers_meters': 1000,
        'grams_kilograms': 0.001,
        'kilograms_grams': 1000,
        'centimeters_millimeters': 10,
        'millimeters_centimeters': 0.1,
    }
    conversion_key = f"{unit_from}{unit_to}"
    return value * conversion.get(conversion_key, 1)

if __name__ == "__main__":
    st.title("Unit Converter")

    value = st.number_input("Enter value:")
    conversion = {
        'meters_kilometers': 0.001,
        'kilometers_meters': 1000,
        'grams_kilograms': 0.001,
        'kilograms_grams': 1000,
        'centimeters_millimeters': 10,
        'millimeters_centimeters': 0.1,
    }
    unitfrom = st.selectbox("Select unit from:", list(set([key.split('_')[0] for key in conversion.keys()])))

    unitto = st.selectbox("Select unit to:", list(set([key.split('_')[1] for key in conversion.keys()])))

    if st.button("Convert"):
        result = convert_units(value, unitfrom, unitto)
        st.success(f"{value} {unitfrom} is equal to {result} {unitto}")
        st.info("Conversion complete!")
        st.write("Thank you for using the Unit Converter!")