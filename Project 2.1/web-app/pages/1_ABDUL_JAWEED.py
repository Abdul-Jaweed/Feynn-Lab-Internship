import streamlit as st

st.header(":blue[Project 1]")

st.title(":red[Indian EV Segmentation]")

st.markdown("""

In India, the electric vehicle (EV) market has been growing rapidly in recent years due to government initiatives and increased environmental awareness. The Indian EV market can be segmented into several categories based on vehicle types and usage patterns. Here are some common segments in the Indian EV market:

- **Two-wheelers:** Two-wheelers are the most popular segment in the Indian EV market. They include electric scooters and motorcycles. Electric two-wheelers are considered an affordable and practical mode of transportation for short distances and urban commuting. They are particularly popular among college students, working professionals, and delivery services.

- **Three-wheelers:** Three-wheelers, also known as auto-rickshaws or e-rickshaws, are widely used for short-distance transportation in urban and semi-urban areas. Electric three-wheelers offer lower operating costs and reduced emissions compared to their conventional counterparts. They are commonly used for last-mile connectivity, shared transportation, and goods delivery.

- **Passenger Cars:** Electric cars are gaining traction in India, especially among urban dwellers and environmentally conscious consumers. Electric passenger cars offer zero tailpipe emissions, lower fuel costs, and government incentives, making them an attractive option. The segment includes hatchbacks, sedans, and compact SUVs.

- **Commercial Vehicles:** The commercial vehicle segment includes electric buses, trucks, and vans. Electric buses are being introduced in various cities as part of public transportation initiatives to reduce pollution and congestion. Electric trucks and vans are gaining popularity for last-mile delivery services, particularly in urban areas.

- **Electric Rickshaws:** Electric rickshaws, also known as e-rickshaws or electric auto-rickshaws, are three-wheeled vehicles used for short-distance transportation. They are typically used for intra-city commuting and are popular in congested areas due to their small size and maneuverability.

- **Electric Bicycles:** Electric bicycles, or e-bikes, are gaining popularity as a sustainable and cost-effective mode of transportation in India. They have a small electric motor that assists the rider's pedaling efforts, allowing for easier and faster commuting. Electric bicycles are commonly used for short trips, leisure rides, and as an alternative to conventional bicycles.



It's important to note that the Indian EV market is evolving rapidly, and new segments and vehicle types may emerge as technology advances and infrastructure improves. Additionally, the government of India has been actively promoting electric mobility through various incentives and policies to encourage the adoption of EVs across all segments.

### Dataset [link](https://www.kaggle.com/datasets/krishnendubarman/indian-ev-segmentation)

            """)


st.header(":blue[Segmentation Chart]")


# col1, col2 = st.columns(2)

# with col1:
#     st.image("images\evafter1.png")
    
# with col2:
#     st.image("images\evbefore1.png")



st.image("images\evbefore2.png")
    

st.image("images\evafter2.png")



st.markdown("""
            #### Code [link](https://github.com/Abdul-Jaweed/Feynn-Lab-Internship/blob/main/Project%202.1/Indian%20EV%20Segmentation.ipynb)
            """)




st.header(":blue[Project 2]")

st.title(":red[Transport Online Vehicle Registration May 2023]")

st.markdown("""
            This dataset provides information about the following details of the vehicles in the state of Telangana.



Contains the below columns: Regn_No: Registration Number Regn_VFDt: Registration Valid From Date Regn_VTDt: Registration Valid To Date Maker_Name: Automobile Maker Name Model_Desc: Vehicle Model Description BodyTyp: Vehicle Body Type CC: Engine Capacity Cylinder: Number of Cylinders in the Vehicle Engine Fuel: Type of Fuel HP: Horse of the Vehicle Seat_Capacity: Seat capacity of the vehicle Apprved_Dt: Approval Date by RTA OfficeCd: Registration Office



### Dataset [link](https://data.telangana.gov.in/dataset/regional-transport-authority-vehicle-registrations-data)
            """)



st.header(":blue[Segmentation Chart]")

st.image("images\evbefore1.png")

st.image("images\evafter1.png")


st.markdown("""
            #### Code [link](https://github.com/Abdul-Jaweed/Feynn-Lab-Internship/blob/main/Project%202.1/Transport%20Online%20Vehicle%20Registration%20May%202023.ipynb)
            """)
