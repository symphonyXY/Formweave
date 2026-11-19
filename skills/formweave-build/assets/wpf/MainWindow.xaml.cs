using System;
using System.Linq;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Input;
using System.Windows.Threading;

namespace Formweave;

public record Item(string Code, string Zone, int Quantity);

public partial class MainWindow : Window
{
    readonly ListCollectionView view;

    public MainWindow()
    {
        InitializeComponent();
        if (SystemParameters.HighContrast)
        {
            Resources["PageBrush"] = Resources["SurfaceBrush"] = Resources["WashBrush"] = SystemColors.WindowBrush;
            Resources["InkBrush"] = Resources["MutedBrush"] = Resources["LineBrush"] = SystemColors.WindowTextBrush;
        }
        view = new ListCollectionView(Enumerable.Range(1, 10000)
            .Select(i => new Item($"FW-{i:D6}", $"A-{(i - 1) % 12 + 1:D2}", i % 87)).ToList());
        Rows.ItemsSource = view;
        RefreshRows();
    }

    void OnSearch(object sender, TextChangedEventArgs args) => RefreshRows();

    void OnSelection(object sender, SelectionChangedEventArgs args)
    {
        if (SelectionInfo == null) return;
        SelectionInfo.Text = Rows.SelectedItem is Item item
            ? $"{item.Code}    ·    {item.Zone} 库区    ·    库存 {item.Quantity} 件"
            : "选择一条记录查看库存。";
    }

    void OnKey(object sender, KeyEventArgs args)
    {
        if (args.Key == Key.F && Keyboard.Modifiers == ModifierKeys.Control)
        {
            Query.Focus();
            Query.SelectAll();
            args.Handled = true;
        }
        else if (args.Key == Key.Escape && Query.IsKeyboardFocusWithin)
        {
            Query.Clear();
            args.Handled = true;
        }
    }

    void RefreshRows()
    {
        if (view == null) return;
        view.Filter = row => ((Item)row).Code.Contains(Query.Text.Trim(), StringComparison.OrdinalIgnoreCase);
        Status.Text = view.Count == 0 ? "没有匹配记录" : $"共 {view.Count:N0} 条记录";
        EmptyHint.Visibility = view.Count == 0 ? Visibility.Visible : Visibility.Collapsed;
    }

    internal bool Probe()
    {
        Query.Focus();
        Query.Text = "FW-010000";
        Width = 445;
        UpdateLayout();
        bool filtered = view.Count == 1 && Rows.ActualWidth > 100 && Query.IsKeyboardFocusWithin;
        Rows.SelectedIndex = 0;
        bool selected = SelectionInfo.Text.Contains("FW-010000");
        Query.Text = "没有该编号";
        bool empty = view.Count == 0 && EmptyHint.IsVisible && Status.Text == "没有匹配记录";
        Query.Clear();
        return filtered && selected && empty && view.Count == 10000;
    }
}

public static class Program
{
    [STAThread]
    public static int Main(string[] args)
    {
        var app = new Application();
        var window = new MainWindow();
        if (args.Contains("--smoke"))
            window.ContentRendered += (_, _) => window.Dispatcher.BeginInvoke(
                DispatcherPriority.ApplicationIdle, new Action(() => app.Shutdown(window.Probe() ? 0 : 2)));
        return app.Run(window);
    }
}
