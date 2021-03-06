from .db import db
from typing import Optional
from pydantic import BaseModel


class Pdf(db.Document):
    redfin_src = db.StringField(required=True, unique=True)
    pdf_src = db.StringField(required=True)
    deleted = db.BooleanField(required=False)


class StaticPdfBody(BaseModel):
    url: str
    refrigerator: Optional[bool]
    refrigerator_details: Optional[str]
    oven_or_range: Optional[bool]
    oven_or_range_details: Optional[str]
    microware: Optional[bool]
    microwave_details: Optional[str]
    dishwasher: Optional[bool]
    dishwasher_details: Optional[str]
    garbage_disposal: Optional[bool]
    garbage_disposal_details: Optional[str]
    trash_compactor: Optional[bool]
    trash_compactor_details: Optional[str]
    washer: Optional[bool]
    washer_details: Optional[str]
    dryer: Optional[bool]
    dryer_details: Optional[str]
    water_softener: Optional[bool]
    water_softner_details: Optional[str]
    sump_pump: Optional[bool]
    sump_pump_details: Optional[str]
    smoke_and_monoxide_detectors: Optional[bool]
    smoke_and_carbon_monoxide_detectors_details: Optional[str]
    intercom_system: Optional[bool]
    intercom_system_details: Optional[str]
    security_system: Optional[bool]
    security_system_details: Optional[str]
    security_system_rented: Optional[bool]
    security_system_owned: Optional[bool]
    satellite_dish: Optional[bool]
    satellite_dish_details: Optional[str]
    attached_tv: Optional[bool]
    attached_tv_details: Optional[str]
    tv_antenna: Optional[bool]
    tv_antenna_details: Optional[str]
    multimedia_equipment: Optional[bool]
    multimedia_equipment_details: Optional[str]
    central_air_conditioner: Optional[bool]
    central_air_conditioner_details: Optional[str]
    window_air_conditioner: Optional[bool]
    window_air_conditioner_details: Optional[str]
    electronic_air_filter: Optional[bool]
    electronic_air_filter_details: Optional[str]
    central_humidifier: Optional[bool]
    central_humidifier_details: Optional[str]
    lighting_fixtures: Optional[bool]
    lighting_fixtures_details: Optional[str]
    electronic_garage_door: Optional[bool]
    electronic_garage_door_with_remote_unit_details: Optional[str]
    tacked_down_carpeting: Optional[bool]
    fireplace_screen_and_equipment: Optional[bool]
    fireplace_screen_and_equipment_details: Optional[str]
    fireplace_gas_log: Optional[bool]
    fireplace_gas_log_details: Optional[str]
    firewood: Optional[bool]
    firewood_details: Optional[str]
    attached_gas_grill: Optional[bool]
    attached_gas_grill_details: Optional[str]
    existing_storms_and_screens: Optional[bool]
    existing_storms_and_screens_details: Optional[str]
    window_treatments: Optional[bool]
    window_treatments_details: Optional[str]
    other_equipment: Optional[bool]
    other_equipment_details: Optional[str]
    built_in_or_attached_shelves_or_cabinets: Optional[bool]
    built_int_or_attached_shelves_or_cabinets_details: Optional[str]
    ceiling_fan: Optional[bool]
    ceiling_fan_details: Optional[str]
    radiator_covers: Optional[bool]
    radiator_covers_details: Optional[str]
    all_planted_vegetation: Optional[bool]
    outdoor_play_set_or_swings: Optional[bool]
    outdoor_shed: Optional[bool]
    purchase_price: Optional[str]
    credit_buyer_at_closing_yes: Optional[bool]
    credit_buyer_at_closing_if_yes_amount: Optional[str]
    credit_buyer_at_closing_no: Optional[bool]
    credit_buyer_at_closing_if_no_percentage: Optional[str]
    home_warranty_amount: Optional[str]
    brokerage_for_earnest_money: Optional[str]
    initial_earnest_money_amount: Optional[str]
    how_buyer_deposits_earnest_money: Optional[str]
    initial_earnest_money_due_date: Optional[str]
    balance_of_earnest_money_amount: Optional[str]
    balance_of_earnest_money_due_date: Optional[str]
    contract_subject_to_mortgage_yes: Optional[bool]
    contract_subject_to_mortgage_no: Optional[bool]
    mortgage_contingency_date: Optional[str]
    buyer_loan_to_value: Optional[str]
    buyer_interest_rate: Optional[str]
    buyer_loan_term: Optional[str]
    closing_date: Optional[str]
    disclosures_a_yes: Optional[bool]
    disclosures_a_no: Optional[bool]
    disclosures_b_yes: Optional[bool]
    disclosures_b_no: Optional[bool]
    disclosures_c_yes: Optional[bool]
    disclosures_c_no: Optional[bool]
    disclosures_d_yes: Optional[bool]
    disclosures_d_no: Optional[bool]
    dual_agent_broker_name: Optional[str]
    length_of_attorney_review: Optional[str]
    length_of_inspection_period: Optional[str]
    offer_date: Optional[str]
    designated_agent: Optional[str]
    agent_mls: Optional[str]
    agent_license: Optional[str]
    brokerage: Optional[str]
    brokerage_mls: Optional[str]
    brokerage_license: Optional[str]
    broker_address: Optional[str]
    agent_phone: Optional[str]
    agent_fax: Optional[str]
    broker_email: Optional[str]
    attorney_name: Optional[str]
    attorney_address: Optional[str]
    attorney_phone: Optional[str]
    attorney_fax: Optional[str]
    attorney_email: Optional[str]
    lender_name: Optional[str]
    lender_company: Optional[str]
    lender_address: Optional[str]
    lender_phone: Optional[str]
    lender_fax: Optional[str]
    lender_email: Optional[str]
