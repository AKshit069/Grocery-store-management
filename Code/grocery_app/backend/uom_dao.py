def get_uoms(connection):
    cursor = connection.cursor()
    query = "SELECT uom_id, uom_name FROM gs.uom"  # Explicitly define columns to avoid issues
    try:
        cursor.execute(query)
        response = []
        for (uom_id, uom_name) in cursor:
            response.append({
                'uom_id': uom_id,
                'uom_name': uom_name
            })
        print(f"Fetched UOMs: {response}")  # Debug print to see fetched UOMs
        return response
    except Exception as e:
        print(f"Error in get_uoms: {e}")
        return {"error": str(e)}  # Return the error for better debugging
    
    
