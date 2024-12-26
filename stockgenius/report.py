def generate_summary_report(df, output_file):
    summary = df.groupby('category').agg({
        'quantity': 'sum',
        'price': 'mean'
    }).reset_index()
    summary.to_csv(output_file, index=False)