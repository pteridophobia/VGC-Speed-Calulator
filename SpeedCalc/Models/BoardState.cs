using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace SpeedCalc.Models
{
    public sealed class BoardState
    {

        public Pokemon leftMon1 { get; set; }
        public Pokemon leftMon2 { get; set; }
        public Pokemon rightMon1 { get; set; }
        public Pokemon rightMon2 { get; set; }

        public Weathers weather { get; set; }
        public Terrains terrain { get; set; }

        public Boolean leftTailwind { get; set; }
        public Boolean rightTailwind { get; set; }
        public Boolean leftSwamp { get; set; }
        public Boolean rightSwamp { get; set; }
        public Boolean leftWeb { get; set; }
        public Boolean rightWeb { get; set; }

        public Boolean trickRoom { get; set; }

        public BoardState()
        {

        }

        public Pokemon[] copmuteTurnOrder()
        {
            Pokemon[] turnOrder = new Pokemon[4];
            // TODO: use stats and boardstate variables to calulate turnorder
            // then insert the left and right pokemon into the array so that 
            // the first pokemon in the list is the first one to move
            return turnOrder;
        }
    }
}
