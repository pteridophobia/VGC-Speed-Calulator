using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace SpeedCalc.Models
{
    public sealed class BoardState
    {
        public Weathers weather;
        public Terrains terrain;

        public Boolean leftTailwind;
        public Boolean rightTailwind;
        public Boolean leftSwamp;
        public Boolean rightSwamp;
        public Boolean leftWeb;
        public Boolean rightWeb;

        public Boolean trickRoom;
        
    }
}
