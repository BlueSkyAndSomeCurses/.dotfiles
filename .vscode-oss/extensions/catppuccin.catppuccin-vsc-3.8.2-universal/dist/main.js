"use strict";Object.defineProperty(exports, "__esModule", {value: true}); function _nullishCoalesce(lhs, rhsFn) { if (lhs != null) { return lhs; } else { return rhsFn(); } }var _chunkSCQBE2JCjs = require('./chunk-SCQBE2JC.js');require('./chunk-LDV6YPMG.js');var _vscode = require('vscode');var w=(e,t)=>Object.fromEntries(Object.entries(e).filter(t)),x=e=>{let t=`Catppuccin: ${e} - Reload required.`,o="Reload window";_vscode.window.showInformationMessage(t,o).then(n=>{n===o&&_vscode.commands.executeCommand("workbench.action.reloadWindow")})},P=async(e,t)=>_vscode.workspace.fs.writeFile(e,Buffer.from(JSON.stringify(t,null,2))).then(()=>{},o=>{_vscode.window.showErrorMessage(o.message)}),O=async e=>_vscode.workspace.fs.stat(e).then(()=>!0,()=>!1);var g=async e=>{console.log("Checking if catppuccin is installed for the first time.");let t=_vscode.Uri.file(e.asAbsolutePath("themes/.flag"));return await O(t)?(console.log("Catppuccin has been installed before."),!1):(console.log("Catppuccin is installed for the first time!"),_vscode.workspace.fs.writeFile(t,Buffer.from("")).then(()=>!0,()=>"error"))},d=()=>{console.log("Checking if catppuccin is using default config.");let e=JSON.stringify(c())===JSON.stringify(_chunkSCQBE2JCjs.b);return console.log(`Catppuccin is using ${e?"default":"custom"} config.`),e},c=()=>{let e=_vscode.workspace.getConfiguration("catppuccin"),t={accent:e.get("accentColor"),boldKeywords:e.get("boldKeywords"),italicKeywords:e.get("italicKeywords"),italicComments:e.get("italicComments"),colorOverrides:e.get("colorOverrides"),workbenchMode:e.get("workbenchMode"),bracketMode:e.get("bracketMode"),extraBordersEnabled:e.get("extraBordersEnabled"),customUIColors:e.get("customUIColors")};return{..._chunkSCQBE2JCjs.b,...w(t,([,o])=>o!==void 0)}},l=async(e,t,o)=>{let a=Object.keys(_chunkSCQBE2JCjs.a).map(async s=>{let C=_chunkSCQBE2JCjs.c.call(void 0, s,e);return P(t[s],C)});Promise.all(a).then(()=>{x(o)})},u=()=>{let e="catppuccin.catppuccin-vsc-icons";if(_vscode.extensions.getExtension(e)===void 0)return;let t={"Catppuccin Latte":"catppuccin-latte","Catppuccin Frapp\xE9":"catppuccin-frappe","Catppuccin Macchiato":"catppuccin-macchiato","Catppuccin Mocha":"catppuccin-mocha"},o=_nullishCoalesce(_vscode.workspace.getConfiguration("workbench").get("colorTheme"), () => ("")),n=Object.keys(t).includes(o),a=Object.values(t).includes(_nullishCoalesce(_vscode.workspace.getConfiguration("workbench").get("iconTheme"), () => ("")));if(n&&a){let s=t[o];_vscode.workspace.getConfiguration("workbench").update("iconTheme",s,_vscode.ConfigurationTarget.Global)}};var S=async e=>{let t=e.extensionUri,o={latte:_vscode.Uri.joinPath(t,"themes","latte.json"),frappe:_vscode.Uri.joinPath(t,"themes","frappe.json"),macchiato:_vscode.Uri.joinPath(t,"themes","macchiato.json"),mocha:_vscode.Uri.joinPath(t,"themes","mocha.json")};await g(e)&&!d()&&l(c(),o,"Update detected"),e.subscriptions.push(_vscode.workspace.onDidChangeConfiguration(n=>{n.affectsConfiguration("catppuccin")&&l(c(),o,"Configuration changed"),n.affectsConfiguration("workbench.colorTheme")&&u()})),u()};exports.activate = S;
