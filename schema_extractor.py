from sqlalchemy import inspect
from database import engine

# Define required columns for each KPI
KPI_REQUIREMENTS = {
    "total_users": {"users": ["id"]},
    "total_events_created": {"events": ["id"]},
    "event_attendance_rate": {"event_users": ["user_id"], "events": ["id"]},
    "average_event_price": {"events": ["price"]},
    "user_engagement_score": {"favorite_events": ["id"], "action_events": ["id"], "users": ["id"]},
    "popular_event_categories": {"category_events": ["event_id", "category_id"]},
    "event_conversion_rate": {"requests": ["id"], "event_users": ["id"]},
    "test_kpi_missing": {"users": ["non_existent_column"]}
}

def get_database_schema():
    inspector = inspect(engine)
    schema = {}

    for table_name in inspector.get_table_names():
        columns = [column["name"] for column in inspector.get_columns(table_name)]
        schema[table_name] = columns

    return schema

def check_kpi_availability():
    schema = get_database_schema()
    missing_columns = {}

    for kpi, tables in KPI_REQUIREMENTS.items():
        for table, required_columns in tables.items():
            if table not in schema:
                missing_columns.setdefault(kpi, []).append(f"Table `{table}` is missing")
            else:
                for column in required_columns:
                    if column not in schema[table]:
                        missing_columns.setdefault(kpi, []).append(f"Column `{column}` is missing in `{table}`")

    return missing_columns
