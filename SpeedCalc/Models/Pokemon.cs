using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace SpeedCalc.Models
{
    public class Pokemon 
    {
        public Mon mon;

        public int level { get; set; }
        public Natures nature { get; set; }

        public Stats EVs { get; set; }
        public Stats IVs { get; set; }
        public Stats modifiers { get; set; }
        public string heldItem { get; set; }
        public string ability { get; set; }

        public Moves move { get; set; }

        public Pokemon (int dex)
        {
            // find mon in data base whose dexNum == dex
            // then call mon(dex)
            //this.mon = mon(dex)

        }

    }
}
