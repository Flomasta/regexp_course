import re

data = '<div class="AkJag"><nav class="uOmOI i1N2B"><a class="HnB3F zOliV PRs2u _eLp0" style="width: 34px; height: 34px;" aria-label="Regex Editor" href="/"><span class="M__Pz">Regex Editor</span><svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24" class="nstWU" height="18" width="18" xmlns="http://www.w3.org/2000/svg"><g><path fill="none" d="M0 0h24v24H0z"></path><path d="M24 12l-5.657 5.657-1.414-1.414L21.172 12l-4.243-4.243 1.414-1.414L24 12zM2.828 12l4.243 4.243-1.414 1.414L0 12l5.657-5.657L7.07 7.757 2.828 12zm6.96 9H7.66l6.552-18h2.128L9.788 21z"></path></g></svg></a><a class="HnB3F PRs2u _eLp0" style="width: 34px; height: 34px;" aria-label="Regex Library" href="/library"><span class="M__Pz">Regex Library</span><svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 512 512" class="nstWU" height="18" width="18" xmlns="http://www.w3.org/2000/svg"><path d="M64 480H48a32 32 0 01-32-32V112a32 32 0 0132-32h16a32 32 0 0132 32v336a32 32 0 01-32 32zm176-304a32 32 0 00-32-32h-64a32 32 0 00-32 32v28a4 4 0 004 4h120a4 4 0 004-4zM112 448a32 32 0 0032 32h64a32 32 0 0032-32v-30a2 2 0 00-2-2H114a2 2 0 00-2 2z"></path><rect width="128" height="144" x="112" y="240" rx="2" ry="2"></rect><path d="M320 480h-32a32 32 0 01-32-32V64a32 32 0 0132-32h32a32 32 0 0132 32v384a32 32 0 01-32 32zm175.89-34.55l-32.23-340c-1.48-15.65-16.94-27-34.53-25.31l-31.85 3c-17.59 1.67-30.65 15.71-29.17 31.36l32.23 340c1.48 15.65 16.94 27 34.53 25.31l31.85-3c17.59-1.67 30.65-15.71 29.17-31.36z"></path></svg></a><a class="HnB3F PRs2u _eLp0" style="width: 34px; height: 34px;" aria-label="Account" href="/account/mine"><span class="M__Pz">Account</span><svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24" class="nstWU" height="18" width="18" xmlns="http://www.w3.org/2000/svg"><g><path fill="none" d="M0 0h24v24H0z"></path><path d="M4 22a8 8 0 1 1 16 0H4zm8-9c-3.315 0-6-2.685-6-6s2.685-6 6-6 6 2.685 6 6-2.685 6-6 6z"></path></g></svg></a><a class="HnB3F PRs2u _eLp0" style="width: 34px; height: 34px;" aria-label="Regex Quiz" href="/quiz"><span class="M__Pz">Regex Quiz</span><svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24" class="nstWU" height="18" width="18" xmlns="http://www.w3.org/2000/svg"><g><path fill="none" d="M0 0h24v24H0z"></path><path d="M17 4a6 6 0 0 1 6 6v4a6 6 0 0 1-6 6H7a6 6 0 0 1-6-6v-4a6 6 0 0 1 6-6h10zm-7 5H8v2H6v2h1.999L8 15h2l-.001-2H12v-2h-2V9zm8 4h-2v2h2v-2zm-2-4h-2v2h2V9z"></path></g></svg></a><a class="HnB3F PRs2u _eLp0" style="width: 34px; height: 34px;" aria-label="Settings" href="/settings"><span class="M__Pz">Settings</span><svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24" class="nstWU" height="18" width="18" xmlns="http://www.w3.org/2000/svg"><path fill="none" d="M0 0h24v24H0V0z"></path><path d="M19.14 12.94c.04-.3.06-.61.06-.94 0-.32-.02-.64-.07-.94l2.03-1.58a.49.49 0 00.12-.61l-1.92-3.32a.488.488 0 00-.59-.22l-2.39.96c-.5-.38-1.03-.7-1.62-.94l-.36-2.54a.484.484 0 00-.48-.41h-3.84c-.24 0-.43.17-.47.41l-.36 2.54c-.59.24-1.13.57-1.62.94l-2.39-.96c-.22-.08-.47 0-.59.22L2.74 8.87c-.12.21-.08.47.12.61l2.03 1.58c-.05.3-.09.63-.09.94s.02.64.07.94l-2.03 1.58a.49.49 0 00-.12.61l1.92 3.32c.12.22.37.29.59.22l2.39-.96c.5.38 1.03.7 1.62.94l.36 2.54c.05.24.24.41.48.41h3.84c.24 0 .44-.17.47-.41l.36-2.54c.59-.24 1.13-.56 1.62-.94l2.39.96c.22.08.47 0 .59-.22l1.92-3.32c.12-.22.07-.47-.12-.61l-2.01-1.58zM12 15.6c-1.98 0-3.6-1.62-3.6-3.6s1.62-3.6 3.6-3.6 3.6 1.62 3.6 3.6-1.62 3.6-3.6 3.6z"></path></svg></a><a href="https://web.libera.chat/?nick=re101-crane-?&amp;chan=#regex" class="HnB3F PRs2u _eLp0" rel="noopener" style="width: 34px; height: 34px;" target="_blank" aria-label="Live Help"><span class="M__Pz">Live Help</span><svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24" class="nstWU" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><g><path fill="none" d="M0 0h24v24H0z"></path><path d="M16.8 19L14 22.5 11.2 19H6a1 1 0 0 1-1-1V7.103a1 1 0 0 1 1-1h16a1 1 0 0 1 1 1V18a1 1 0 0 1-1 1h-5.2zM2 2h17v2H3v11H1V3a1 1 0 0 1 1-1z"></path></g></svg></a></nav><div class="hIvL6"><div class="wcfss"><h2 class="dYInr JOzNE z2wCE bjLBV"><span class="JOzNE">Save &amp; Share</span></h2><ul class="yEXrR"><li class="b0Wk4 tu7rF" aria-disabled="false" role="button" tabindex="0"><div class="WLU1r BcuOd VZGjx wHTes"><svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24" class="FvZHv" height="14" width="14" xmlns="http://www.w3.org/2000/svg"><g><path fill="none" d="M0 0h24v24H0z"></path><path d="M18 21v-8H6v8H4a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1h13l4 4v13a1 1 0 0 1-1 1h-2zm-2 0H8v-6h8v6z"></path></g></svg><div class="Lta24">Save Regex</div><div class="IVPLo">ctrl+s</div></div></li></ul></div><div class="wcfss"><h2 class="dYInr JOzNE z2wCE bjLBV"><span class="JOzNE">Flavor</span><a class="HnB3F kKIV1 PRs2u IC7U1" style="width: 16px; height: 16px;" aria-label="Need help selecting flavor?" href="/static/assets/flavors.md"><span class="M__Pz">Need help selecting flavor?</span><svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24" class="nstWU" height="16" width="16" xmlns="http://www.w3.org/2000/svg"><g><path fill="none" d="M0 0h24v24H0z"></path><path d="M12 22C6.477 22 2 17.523 2 12S6.477 2 12 2s10 4.477 10 10-4.477 10-10 10zm0-2a8 8 0 1 0 0-16 8 8 0 0 0 0 16zm-1-5h2v2h-2v-2zm2-1.645V14h-2v-1.5a1 1 0 0 1 1-1 1.5 1.5 0 1 0-1.471-1.794l-1.962-.393A3.501 3.501 0 1 1 13 13.355z"></path></g></svg></a></h2><ul class="yEXrR"><li class="b0Wk4 tu7rF" role="button" tabindex="0"><div class="WLU1r BcuOd"><svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24" class="FvZHv" height="14" width="14" xmlns="http://www.w3.org/2000/svg"><g><path fill="none" d="M0 0h24v24H0z"></path><path d="M24 12l-5.657 5.657-1.414-1.414L21.172 12l-4.243-4.243 1.414-1.414L24 12zM2.828 12l4.243 4.243-1.414 1.414L0 12l5.657-5.657L7.07 7.757 2.828 12zm6.96 9H7.66l6.552-18h2.128L9.788 21z"></path></g></svg><div class="rocdx"><div class="u_Q0A">PCRE2 (PHP &gt;=7.3)</div></div></div></li><li class="b0Wk4 tu7rF" role="button" tabindex="0"><div class="WLU1r BcuOd"><svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24" class="FvZHv" height="14" width="14" xmlns="http://www.w3.org/2000/svg"><g><path fill="none" d="M0 0h24v24H0z"></path><path d="M24 12l-5.657 5.657-1.414-1.414L21.172 12l-4.243-4.243 1.414-1.414L24 12zM2.828 12l4.243 4.243-1.414 1.414L0 12l5.657-5.657L7.07 7.757 2.828 12zm6.96 9H7.66l6.552-18h2.128L9.788 21z"></path></g></svg><div class="rocdx"><div class="u_Q0A">PCRE (PHP &lt;7.3)</div></div></div></li><li class="b0Wk4 tu7rF" role="button" tabindex="0"><div class="WLU1r BcuOd"><svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24" class="FvZHv" height="14" width="14" xmlns="http://www.w3.org/2000/svg"><g><path fill="none" d="M0 0h24v24H0z"></path><path d="M24 12l-5.657 5.657-1.414-1.414L21.172 12l-4.243-4.243 1.414-1.414L24 12zM2.828 12l4.243 4.243-1.414 1.414L0 12l5.657-5.657L7.07 7.757 2.828 12zm6.96 9H7.66l6.552-18h2.128L9.788 21z"></path></g></svg><div class="rocdx"><div class="u_Q0A">ECMAScript (JavaScript)</div></div></div></li><li class="b0Wk4 tu7rF" role="button" tabindex="0"><div class="WLU1r BcuOd"><svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24" class="FvZHv" height="14" width="14" xmlns="http://www.w3.org/2000/svg"><g><path fill="none" d="M0 0h24v24H0z"></path><path d="M24 12l-5.657 5.657-1.414-1.414L21.172 12l-4.243-4.243 1.414-1.414L24 12zM2.828 12l4.243 4.243-1.414 1.414L0 12l5.657-5.657L7.07 7.757 2.828 12zm6.96 9H7.66l6.552-18h2.128L9.788 21z"></path></g></svg><div class="rocdx wxNpu"><div class="u_Q0A">Python</div><svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24" class="zxc_j" height="16" width="16" xmlns="http://www.w3.org/2000/svg"><g><path fill="none" d="M0 0h24v24H0z"></path><path d="M10 15.172l9.192-9.193 1.415 1.414L10 18l-6.364-6.364 1.414-1.414z"></path></g></svg></div></div></li><li class="b0Wk4 tu7rF" role="button" tabindex="0"><div class="WLU1r BcuOd"><svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24" class="FvZHv" height="14" width="14" xmlns="http://www.w3.org/2000/svg"><g><path fill="none" d="M0 0h24v24H0z"></path><path d="M24 12l-5.657 5.657-1.414-1.414L21.172 12l-4.243-4.243 1.414-1.414L24 12zM2.828 12l4.243 4.243-1.414 1.414L0 12l5.657-5.657L7.07 7.757 2.828 12zm6.96 9H7.66l6.552-18h2.128L9.788 21z"></path></g></svg><div class="rocdx"><div class="u_Q0A">Golang</div></div></div></li><li class="b0Wk4 tu7rF" role="button" tabindex="0"><div class="WLU1r BcuOd"><svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24" class="FvZHv" height="14" width="14" xmlns="http://www.w3.org/2000/svg"><g><path fill="none" d="M0 0h24v24H0z"></path><path d="M24 12l-5.657 5.657-1.414-1.414L21.172 12l-4.243-4.243 1.414-1.414L24 12zM2.828 12l4.243 4.243-1.414 1.414L0 12l5.657-5.657L7.07 7.757 2.828 12zm6.96 9H7.66l6.552-18h2.128L9.788 21z"></path></g></svg><div class="rocdx"><div class="u_Q0A">Java 8</div></div></div></li><li class="b0Wk4 tu7rF" role="button" tabindex="0"><div class="WLU1r BcuOd"><svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24" class="FvZHv" height="14" width="14" xmlns="http://www.w3.org/2000/svg"><g><path fill="none" d="M0 0h24v24H0z"></path><path d="M24 12l-5.657 5.657-1.414-1.414L21.172 12l-4.243-4.243 1.414-1.414L24 12zM2.828 12l4.243 4.243-1.414 1.414L0 12l5.657-5.657L7.07 7.757 2.828 12zm6.96 9H7.66l6.552-18h2.128L9.788 21z"></path></g></svg><div class="rocdx"><div class="u_Q0A">.NET (C#)</div></div></div></li></ul></div><div class="wcfss"><h2 class="dYInr JOzNE z2wCE bjLBV"><span class="JOzNE">Function</span></h2><ul class="yEXrR"><li class="b0Wk4 tu7rF" role="button" tabindex="0"><div class="WLU1r BcuOd"><svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24" class="FvZHv" height="14" width="14" xmlns="http://www.w3.org/2000/svg"><g><path fill="none" d="M0 0h24v24H0z"></path><path d="M11 12l-7.071 7.071-1.414-1.414L8.172 12 2.515 6.343 3.929 4.93 11 12zm0 7h10v2H11v-2z"></path></g></svg><div class="rocdx wxNpu"><div class="u_Q0A">Match</div><svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24" class="zxc_j" height="16" width="16" xmlns="http://www.w3.org/2000/svg"><g><path fill="none" d="M0 0h24v24H0z"></path><path d="M10 15.172l9.192-9.193 1.415 1.414L10 18l-6.364-6.364 1.414-1.414z"></path></g></svg></div></div></li><li class="b0Wk4 tu7rF" role="button" tabindex="0"><div class="WLU1r BcuOd"><svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24" class="FvZHv" height="14" width="14" xmlns="http://www.w3.org/2000/svg"><g><path fill="none" d="M0 0h24v24H0z"></path><path d="M9.683 7.562L12 9.88l6.374-6.375a2 2 0 0 1 2.829 0l.707.707L9.683 16.438a4 4 0 1 1-2.121-2.121L9.88 12 7.562 9.683a4 4 0 1 1 2.121-2.121zM6 8a2 2 0 1 0 0-4 2 2 0 0 0 0 4zm0 12a2 2 0 1 0 0-4 2 2 0 0 0 0 4zm9.535-6.587l6.375 6.376-.707.707a2 2 0 0 1-2.829 0l-4.96-4.961 2.12-2.122z"></path></g></svg><div class="rocdx"><div class="u_Q0A">Substitution</div></div></div></li><li class="b0Wk4 tu7rF" role="button" tabindex="0"><div class="WLU1r BcuOd"><svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24" class="FvZHv" height="14" width="14" xmlns="http://www.w3.org/2000/svg"><g><path fill="none" d="M0 0h24v24H0z"></path><path d="M2 18h7v2H2v-2zm0-7h9v2H2v-2zm0-7h20v2H2V4zm18.674 9.025l1.156-.391 1 1.732-.916.805a4.017 4.017 0 0 1 0 1.658l.916.805-1 1.732-1.156-.391c-.41.37-.898.655-1.435.83L19 21h-2l-.24-1.196a3.996 3.996 0 0 1-1.434-.83l-1.156.392-1-1.732.916-.805a4.017 4.017 0 0 1 0-1.658l-.916-.805 1-1.732 1.156.391c.41-.37.898-.655 1.435-.83L17 11h2l.24 1.196c.536.174 1.024.46 1.434.83zM18 18a2 2 0 1 0 0-4 2 2 0 0 0 0 4z"></path></g></svg><div class="rocdx"><div class="u_Q0A">List</div></div></div></li><li class="b0Wk4 tu7rF" role="button" tabindex="0"><div class="WLU1r BcuOd"><svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24" class="FvZHv" height="14" width="14" xmlns="http://www.w3.org/2000/svg"><g><path fill="none" d="M0 0H24V24H0z"></path><path d="M17 2v2h-1v14c0 2.21-1.79 4-4 4s-4-1.79-4-4V4H7V2h10zm-4 13c-.552 0-1 .448-1 1s.448 1 1 1 1-.448 1-1-.448-1-1-1zm-2-3c-.552 0-1 .448-1 1s.448 1 1 1 1-.448 1-1-.448-1-1-1zm3-8h-4v4h4V4z"></path></g></svg><div class="rocdx"><div class="u_Q0A">Unit Tests </div></div></div></li></ul></div><div><h2 class="dYInr JOzNE z2wCE bjLBV"><span class="JOzNE">Tools</span></h2><ul class="yEXrR"><li class="tu7rF"><a class="HnB3F PEVyC" href="/codegen?language=python"><div class="WLU1r BcuOd"><svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16" class="FvZHv" height="14" width="14" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M10.57 1.14l3.28 3.3.15.36v9.7l-.5.5h-11l-.5-.5v-13l.5-.5h7.72l.35.14zM10 5h3l-3-3v3zM3 2v12h10V6H9.5L9 5.5V2H3zm2.062 7.533l1.817-1.828L6.17 7 4 9.179v.707l2.171 2.174.707-.707-1.816-1.82zM8.8 7.714l.7-.709 2.189 2.175v.709L9.5 12.062l-.705-.709 1.831-1.82L8.8 7.714z"></path></svg>Code Generator</div></a></li></ul></div></div></div>'

pattern = r'(?:(?<=<)|(?<=<\/))([a-z\d]+)'
print(re.findall(pattern, data))