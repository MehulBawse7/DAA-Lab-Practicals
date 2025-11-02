import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Optimal Advertisement Slot Booking")
root.geometry("500x450")
root.config(bg="#f0f4f7")

ads = []

def add_ad():
    try:
        s = int(start_entry.get())
        e = int(end_entry.get())
        p = int(profit_entry.get())
        if s >= e or p <= 0:
            messagebox.showerror("Invalid Input", "End time must be greater than start time and profit positive.")
            return
        ads.append((s, e, p))
        ad_list.insert(tk.END, f"Ad {len(ads)}: Start={s}, End={e}, Profit={p}")
        start_entry.delete(0, tk.END)
        end_entry.delete(0, tk.END)
        profit_entry.delete(0, tk.END)
    except:
        messagebox.showerror("Error", "Please enter valid integers.")

def calculate_optimal_profit():
    if not ads:
        messagebox.showinfo("No Ads", "Please add at least one advertisement.")
        return

    
    sorted_ads = sorted(ads, key=lambda x: x[1])
    n = len(sorted_ads)
    dp = [0] * n
    parent = [-1] * n   

    def find_last_non_conflict(i):
        for j in range(i - 1, -1, -1):
            if sorted_ads[j][1] <= sorted_ads[i][0]:
                return j
        return -1

    dp[0] = sorted_ads[0][2]

    for i in range(1, n):
        incl = sorted_ads[i][2]
        l = find_last_non_conflict(i)
        if l != -1:
            incl += dp[l]
        if incl > dp[i - 1]:
            dp[i] = incl
            parent[i] = l
        else:
            dp[i] = dp[i - 1]
            parent[i] = parent[i - 1]

    
    selected_ads = []
    i = n - 1
    while i >= 0:
        l = find_last_non_conflict(i)
        incl_profit = sorted_ads[i][2] + (dp[l] if l != -1 else 0)
        if incl_profit > (dp[i - 1] if i >= 1 else 0):
            selected_ads.append(sorted_ads[i])
            i = l
        else:
            i -= 1
    selected_ads.reverse()

    
    result_msg = f"Maximum obtainable revenue: {dp[-1]}\n\nSelected Ads:\n"
    for idx, ad in enumerate(selected_ads, start=1):
        result_msg += f"Ad {idx}: Start={ad[0]}, End={ad[1]}, Profit={ad[2]}\n"

    messagebox.showinfo("Optimal Selection", result_msg)

title_label = tk.Label(root, text="Optimal Advertisement Slot Booking",
                       font=("Arial", 14, "bold"), bg="#f0f4f7", fg="#2a5d84")
title_label.pack(pady=10)

frame = tk.Frame(root, bg="#f0f4f7")
frame.pack(pady=10)

tk.Label(frame, text="Start Time:", bg="#f0f4f7").grid(row=0, column=0, padx=5, pady=5)
start_entry = tk.Entry(frame)
start_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="End Time:", bg="#f0f4f7").grid(row=1, column=0, padx=5, pady=5)
end_entry = tk.Entry(frame)
end_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="Profit:", bg="#f0f4f7").grid(row=2, column=0, padx=5, pady=5)
profit_entry = tk.Entry(frame)
profit_entry.grid(row=2, column=1, padx=5, pady=5)

add_btn = tk.Button(root, text="Add Advertisement", command=add_ad,
                    bg="#2a5d84", fg="white", relief="groove", width=20)
add_btn.pack(pady=10)

ad_list = tk.Listbox(root, width=50, height=8, bg="white", fg="#333", font=("Consolas", 10))
ad_list.pack(pady=10)

calc_btn = tk.Button(root, text="Calculate Optimal Revenue", command=calculate_optimal_profit,
                     bg="#007b5e", fg="white", relief="groove", width=25)
calc_btn.pack(pady=10)

root.mainloop()