def predict_expenses(df):
    # Process and predict (placeholder)
    total = df['Amount'].sum()
    groceries = df[df['Category'] == 'Groceries']['Amount'].sum()
    return {
        'total': total,
        'groceries': groceries,
        'advice': f"Groceries spending in July: ₹{groceries}. Try reducing it by 15%."
    }
